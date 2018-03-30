# IBM-Model1-mechine-translation

本项目基于‘statistical mechine translation’一书中4.2节的图4.3算法实现<br>

主要包含4个py文件：run.py, data_processing.py, print_result.py, IBM_algorithm.py<br>

data\_processing.py是对数据进行预处理，输入文件是2个文件，每行相互对应，并且已经分好词。<br>

IBM\_algorithm.py是核心算法，Init是初始化t，IBMAlgorithm是算法的核心步骤，基本按照图4.3实现。在代码11-16行注释是将native word对应到NULL的过程去掉，如果不去掉，发现最终结果t的topN都是某一native word对应于NULL<br>

run.py是算法运行的主文件，会运行上述两个py文件。<br>

print\_result.py是打印结果的代码，可以将t中topN的对应结果输出，并打印到output中。<br><br>

如发现算法存在问题，请联系shucunt@163.com，谢谢！<br>

