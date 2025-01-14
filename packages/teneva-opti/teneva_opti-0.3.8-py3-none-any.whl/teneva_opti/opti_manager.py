import numpy as np
import os


from .bm_view import BmView
from .plot import plot_deps
from .utils import Log
from .utils import get_identity_str
from .utils import path


class OptiManager:
    def __init__(self, tasks=[], fold='result', machine='', is_show=False):
        self.tasks = tasks
        self.fold = fold
        self.machine = machine
        self.is_show = is_show

        fname = 'log_manager_show' if self.is_show else 'log_manager'
        fpath = os.path.join(self.fold, fname)
        self.log = Log(fpath, is_file_add=is_show)

        self.bms = []

    def build_args(self, args, bm):
        args['bm'] = args.get('bm', bm)
        args['fold'] = args.get('fold', self.fold)
        args['log'] = args.get('log', False)
        args['log_info'] = args.get('log_info', True)
        args['log_file'] = args.get('log_file', True)
        args['machine'] = args.get('machine', self.machine)
        return args

    def check_table(self):
        bm_names = []
        for bm in self.bms:
            bm_names.append(bm.bm_name)
        bm_names = list(set(bm_names))
        if len(bm_names) > 1:
            raise ValueError(f'Invalid (more than 1 bm name for table)')
        bm_name = bm_names[0]

        ops = {}
        for bm in self.bms:
            ops[bm.op_name] = ops.get(bm.op_name, 0) + 1
        for name, count in ops.items():
            if count > 1:
                raise ValueError(f'Invalid for opti "{name}" (repeated)')

    def filter(self, arg='name', value=None, is_op=False):
        if value is None:
            return

        bms = []
        for bm in self.bms:
            config = getattr(bm, 'op_config' if is_op else 'bm_config', {})
            value_ref = config.get(arg)
            if value == value_ref:
                bms.append(bm)

        self.bms = bms

    def filter_by_bm(self, arg='name', value=None):
        self.filter(arg, value, is_op=False)

    def filter_by_op(self, arg='name', value=None):
        self.filter(arg, value, is_op=True)

    def get_best(self, kind, is_time):
        value_best = None
        for bm in self.bms:
            if bm.is_better(value_best, kind, is_time):
                value_best = bm.get(kind, is_time)
        return value_best

    def info(self, bm, opti, len_max=21):
        text = ''

        name = bm.name[:(len_max-1)]
        text += '\n'
        text += '- BM   > ' + name + ' '*(len_max-len(name))
        text += ' [' + get_identity_str(bm, pretty=True) + ']'

        name = opti.name[:(len_max-1)]
        text += '\n'
        text += '- OPTI > ' + name + ' '*(len_max-len(name))
        text += ' [' + get_identity_str(opti, pretty=True) + ']'

        return text

    def info_history(self, opti, len_max=27):
        text = '  >>>>>> '

        if opti.is_fail:
            text += f'FAIL'
        else:
            task = 'max' if opti.is_max else 'min'
            text += f'{task}: {opti.y_opt:-14.5e}   '
            text += f'[time: {opti.time_full:-8.1e}]'

        return text

    def join_by_op_seed(self):
        bms = []
        for bm in self.bms:
            is_found = False
            for bmg in bms:
                if bmg.is_same(bm):
                    bmg.add(bm)
                    is_found = True
                    break
            if not is_found:
                bmg = BmView()
                bmg.add(bm)
                bms.append(bmg)

        self.bms = bms

    def load(self):
        self.bms = []

        def opts_str_to_dict(opts_str):
            opts = {}
            for opt_str in opts_str.split('__'):
                opt_list = opt_str.split('-')
                id = opt_list[0]
                if len(opt_list) > 1:
                    try:
                        v = int(opt_list[1])
                    except Exception as e:
                        v = opt_list[1]
                else:
                    v = True
                opts[id] = v
            return opts

        def check(data):
            if data['bm_name'] != data['config']['bm']['name']:
                raise ValueError('Invalid data')

            if data['op_name'] != data['config']['name']:
                raise ValueError('Invalid data')

            for id, v in data['bm_opts'].items():
                if not id in data['config']['bm']:
                    raise ValueError('Invalid data')
                if v != data['config']['bm'][id]:
                    raise ValueError('Invalid data')

            for id, v in data['op_opts'].items():
                if not id in data['config']:
                    raise ValueError('Invalid data')
                if v != data['config'][id]:
                    raise ValueError('Invalid data')

        fold1 = self.fold
        for bm_name in os.listdir(fold1):
            fold2 = os.path.join(fold1, bm_name)
            if  bm_name[0] == '_' or os.path.isfile(fold2):
                continue
            fold3 = os.path.join(fold2, 'data')
            for bm_opts_str in os.listdir(fold3):
                fold4 = os.path.join(fold3, bm_opts_str)
                if os.path.isfile(fold4):
                    continue
                for op_opts_str in os.listdir(fold4):
                    fold5 = os.path.join(fold4, op_opts_str)
                    if os.path.isfile(fold5):
                        continue
                    for op_file in os.listdir(fold5):
                        if not '.npz' in op_file:
                            continue
                        op_name = op_file.split('.npz')[0]
                        op_path = os.path.join(fold5, op_file)
                        data = np.load(op_path, allow_pickle=True)
                        data = data.get('data').item()
                        data['bm_opts'] = opts_str_to_dict(bm_opts_str)
                        data['op_opts'] = opts_str_to_dict(op_opts_str)
                        data['bm_name'] = bm_name
                        data['op_name'] = op_name
                        check(data)
                        self.bms.append(BmView(data))

    def run(self):
        for task in self.tasks:
            # Create Bm class instance:
            Bm = task['bm']
            args = task.get('bm_args', {})
            bm = Bm(**args)
            if 'bm_opts' in task:
                bm.set_opts(**task['bm_opts'])
            if 'bm_seed' in task:
                # TODO: seed should be the argument of bm.__init__
                bm.set_seed(task['bm_seed'])

            # Create Opti class instance:
            Opti = task['opti']
            args = task.get('opti_args', {})
            args = self.build_args(args, bm)
            opti = Opti(**args)
            if 'opti_opts' in task:
                opti.set_opts(**task['opti_opts'])

            # Run the optimization:
            self.log(self.info(bm, opti))
            opti.run(with_err=False)
            self.log(self.info_history(opti))

            # Save the results:
            opti.save()
            if not opti.is_fail:
                opti.render(with_wrn=False)
                opti.show(with_wrn=False)

    def show_plot(self, fpath=None, name_map=None, name_spec=None, colors=None,
                  scale=1., lim_x=None, lim_y=None):
        """This is draft!!!"""
        self.check_table()

        if colors is None:
            colors = [
                '#000099', '#FFB300', '#00B454', '#cc0000', '#cc6699',
                '#804000', '#ff66ff', '#333300',
                '#003300', '#FFF800', '#CE0071', '#333300', '#66ffcc',
                '#ff9999', '#6699ff', '#804000', '#558000']

        data = {}
        for bm in self.bms:
            name = name_map[bm.op_name] if name_map else bm.op_name
            data[name] = {
                'best': np.array(bm.y_all_best) / scale,
                'mean': np.array(bm.y_all_mean) / scale,
                'wrst': np.array(bm.y_all_wrst) / scale,
                'skip': bm.is_fail}

        plot_deps(data, colors, path(fpath, 'png'), name_spec,
            lim_x=lim_x, lim_y=lim_y)

    def show_table(self, prefix='', postfix='', prec=2, kind='mean',
                   is_time=False, prefix_inner='        & ', fail='FAIL',
                   best_cmd='fat', postfix_inner='',
                   prefix_comment_inner='%       > ', with_comment=False):
        self.check_table()
        value_best = self.get_best(kind, is_time)

        if prefix:
            self.log(prefix)
        for bm in self.bms:
            self.log(bm.info_table(prec, value_best, kind, is_time,
                prefix_inner, fail, best_cmd, postfix_inner,
                prefix_comment_inner, with_comment))
        if postfix:
            self.log(postfix)

    def show_text(self, prec=5, prec_time=1):
        for bm in self.bms:
            self.log(bm.info_text(prec, prec_time))

    def sort(self, arg='name', values=None, is_op=False):
        def sort(bm):
            config = getattr(bm, 'op_config' if is_op else 'bm_config', {})
            value = config.get(arg)
            if values is None:
                return value
            else:
                return values.index(value) if value in values else len(values)
        self.bms = sorted(self.bms, key=lambda bm: sort(bm))

    def sort_by_bm(self, arg='name', values=None):
        self.sort(arg, values, is_op=False)

    def sort_by_op(self, arg='name', values=None):
        self.sort(arg, values, is_op=True)
