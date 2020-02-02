import logging
logging.basicConfig(level=10,
         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
             filename=r'text.log')      # filename 是将信息写入 text.log  文件中
logging.debug('debug message') # 排错
logging.info('info message') # 正常信息
logging.warning('warning message') # 警告
logging.error('error message') # 错误
logging.critical('critical message') # 崩溃
