import logging
class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger()
        if not logger.hasHandlers():  # ✅ Avoid adding multiple handlers
            log_file = logging.FileHandler(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Logs\CredKart_Automation.log", mode='a')
            log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d -  %(message)s')
            log_file.setFormatter(log_format)
            logger.addHandler(log_file)
            logger.setLevel(logging.INFO)
        return logger