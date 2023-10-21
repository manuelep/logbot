from dotenv import load_dotenv
import argparse
from pathlib import Path
import os

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="""My Log Bot""",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("-e", "--env-file",
        dest = 'env',
        default = None,
        help="Path to env file"
    )

    parser.add_argument("-m", "--message",
        default = 'ciao',
        help="Message"
    )

    parser.add_argument("-l", "--level",
        default = 'info',
        help="Message"
    )
    
    parser.add_argument("-w", "--welcome",
        action="store_false",
        default=True,
        help="Send welcome message on logging start",
    )

    args = parser.parse_args()
    
    # breakpoint()
    
    if args.env:
        load_dotenv(Path(args.env))
    else:
        load_dotenv()

    os.environ["DBNET"] = 'localhost'
    os.environ['DB_MIGRATE'] = 'False'

    import logbot.logging

    logger = logbot.logging.get_logger(welcome=args.welcome)

    getattr(logger, args.level)(args.message)
