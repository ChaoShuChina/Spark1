from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster('local').setAppName("my app")
sc = SparkContext(conf = conf)
rdd = sc.textFile("/home/chao-shu/1spark/wordcot.txt")
words = rdd.flatMap(lambda x : x.split(" "))
# print words.collect()
result = words.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
print result.collect()
mm = sc.parallelize([("a",7),("b",4),("c",9),("a",110),("c",12)])
print mm.collect()
sumCount = mm.combineByKey((lambda x:(x,1)),
                               (lambda x,y:(x[0] + y,x[1] + 1)),
                               (lambda x,y:(x[0] + y[0],x[1] + y[1])))
print sumCount.collect()
sumCount.map(lambda key,xy:(key,xy[0]/xy[1])).collect()
