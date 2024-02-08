
from real_oram.ORAM import ORAM
from real_oram.RAM.local_RAM import local_RAM, reset_counters
from loading_bar import update_loading_bar
from real_oram.config import config
from LogExecutionTime import ExecutionTimeLogger
import os
#our ORAM test
def _real_oram_test(oram_size):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    oram = ORAM(oram_size)
    oram.cleanWriteMemory()
    # allocating memory shouldn't count as 'writing'...
    reset_counters()
    path_init = 'logs/log_initial_build_number_of_blocks_'+str(oram_size)+' block_size_'+str(config.BALL_DATA_SIZE)+'_bytes.txt'
    logger_init = ExecutionTimeLogger(path_init)
    logger_init.start()
    oram.initial_build('testing_data')
    logger_init.stop_and_log("Initial build time ", oram_size)
    # check if the log directory exists
    
    path_access = 'logs/log_accesses_number_of_blocks_'+str(oram_size)+' block_size_'+str(config.BALL_DATA_SIZE)+'_bytes.txt'
    logger = ExecutionTimeLogger(path_access)
    logger.start()
    for i in range(int(oram_size)-1):
        oram.access('write',int(i).to_bytes(oram.conf.KEY_SIZE,'big'),int(i+3).to_bytes(oram.conf.BALL_DATA_SIZE,'big'))
        if i % 10_000 == 0:
            update_loading_bar(i/oram_size)
    logger.stop_and_log("Access time ", oram_size)
   
    # print the total time in nanoseconds
    # print('Total time:', total_time, 'seconds')
    # print('Average time per access:', total_time/oram_size, 'seconds')
    # print('Average time per access:', total_time/oram_size*10**9, 'nanoseconds')
    # # average time per access divided by oram_size
    # print('Average time per access:', total_time/oram_size, 'seconds')
    # print('Average time per access:', total_time/oram_size*10**9, 'nanoseconds')


def real_oram_test(numberOfBlocks):
    # number_of_MB = int(input('How many MB of storage should the test allocate?\n'))

    # The amount of data in each block is 16 bytes
    # number_of_blocks = int((number_of_MB*(2**20))/16)
    # number_of_blocks = int((number_of_MB*(2**20))/config.BALL_DATA_SIZE)
    number_of_blocks = numberOfBlocks
    number_of_MB = number_of_blocks*config.BALL_DATA_SIZE/(2**20)
    print('Executing',number_of_blocks,'accesses (the size of the ORAM as every block contains 16bytes of data)')
    if number_of_MB > 50:
        print('Due to the initial build it might take several minutes before accesses begin.')
    
    if number_of_MB > 1000:
        print('Due to the initial build it might take several hours before accesses begin.')
    
    _real_oram_test(number_of_blocks)
    
    print('\naccesses: ', number_of_blocks) 
    
    Blocks_read = local_RAM.BALL_READ+local_RAM.BALL_WRITE
    print('Blocks-read: ', Blocks_read)
    
    print('Average blocks read per-access:', int(Blocks_read/number_of_blocks), 'Blocks')
    
    # The multiplication and then division of 10 is to make it show only one digit after the decimal point
    print('Average KB per-access:', int((10*32*Blocks_read/number_of_blocks)/1024)/10, 'KB')

    # Here we divide by 2 because the definition of a round trip is read-process-write
    print('Average round-trips per-access:', int((local_RAM.RT_READ+local_RAM.RT_WRITE)/(2*number_of_blocks)))


