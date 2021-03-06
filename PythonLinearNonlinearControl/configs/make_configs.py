from .first_order_lag import FirstOrderLagConfigModule
from .two_wheeled import TwoWheeledConfigModule

def make_config(args):
    """
    Returns:
        config (ConfigModule class): configuration for the each env
    """
    if args.env == "FirstOrderLag":
        return FirstOrderLagConfigModule()
    elif args.env == "TwoWheeledConst" or args.env == "TwoWheeled":
        return TwoWheeledConfigModule()