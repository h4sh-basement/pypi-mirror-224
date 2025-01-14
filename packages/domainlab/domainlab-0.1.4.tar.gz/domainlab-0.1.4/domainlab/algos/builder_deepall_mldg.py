"""
builder for domain invariant adversarial learning
"""
from domainlab.algos.a_algo_builder import NodeAlgoBuilder
from domainlab.algos.msels.c_msel_val import MSelValPerf
from domainlab.algos.observers.b_obvisitor import ObVisitor
from domainlab.algos.trainers.train_mldg import TrainerMLDG
from domainlab.compos.zoo_nn import FeatExtractNNBuilderChainNodeGetter
from domainlab.models.model_deep_all import mk_deepall
from domainlab.utils.utils_cuda import get_device


class NodeAlgoBuilderDeepAllMLDG(NodeAlgoBuilder):
    """
    builder for domain invariant adversarial learning
    """
    def init_business(self, exp):
        """
        return trainer, model, observer
        """
        task = exp.task
        args = exp.args
        device = get_device(args)
        model_sel = MSelValPerf(max_es=args.es)
        observer = ObVisitor(exp, model_sel, device)

        builder = FeatExtractNNBuilderChainNodeGetter(
            args, arg_name_of_net="nname",
            arg_path_of_net="npath")()  # request, # @FIXME, constant string

        net = builder.init_business(flag_pretrain=True, dim_out=task.dim_y,
                                    remove_last_layer=False, args=args,
                                    i_c=task.isize.i_c,
                                    i_h=task.isize.i_h,
                                    i_w=task.isize.i_w)

        model = mk_deepall()(net, list_str_y=task.list_str_y)
        trainer = TrainerMLDG()
        trainer.init_business(model, task, observer, device, args)
        return trainer
