from itertools import count
import os
import numpy as np
import math
# contourStep=20
# minDistance1=500
# minDistance2=500
# slope = math.atan(contourStep / minDistance1) / math.pi * 180 / 2 + math.atan(contourStep / minDistance2) / math.pi * 180 / 2
# print(slope)
from docx import Document
### transfer one Docx to txt
def transferDocxToTxt(file):
    doc = Document(file)
    # 提取文本内容
    text = []
    for paragraph in doc.paragraphs:
        text.append( paragraph.text+"\n")
    # 使用Python内置的文件写入功能保存文本内容
    with open(file.replace('.docx', '.txt'), "w", encoding="utf-8") as output_file:
        output_file.writelines(text)
### transfer every docx in the directory to corresponding txt
def transferDocxSToTxt(directory):
    # 遍历目标目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以.docx为后缀
        if filename.endswith(".docx"):
            # 构造完整的文件路径
            file_path = os.path.join(directory, filename)
            transferDocxToTxt(file_path) 
#---------transfer  docx  to corresponding txt---------------------------------------------------
# #transfer  docx  to corresponding txt
# directory = "./dataTokenCls_SentencenSegmentation/data/docx"
# file = "./dataTokenCls_SentencenSegmentation/data/docx/Coverletter.docx"
# # transferDocxToTxt(file)
# transferDocxSToTxt(directory)


# #####--------------------transfer excel to txt-------------------------------
# import pandas as pd  
# # Excel文件路径  
# excel_file_path = r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\weibo\train.csv'  
# # 输出的txt文件路径  
# txt_file_path = r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\weibo\train.txt'  
# # 存放vocab的目录  
# column_name = 'review'  # 假设你要提取的是第3列，列名为'Column3'  
# # 使用pandas读取Excel文件的第3列（假设列名为'Column3'）  
# df = pd.read_csv(excel_file_path, usecols=[column_name])  
  
# # 将第3列的内容写入txt文件  
# with open(txt_file_path, 'w', encoding='utf-8') as f:  
#     for item in df[column_name]:  
#         f.write("%s\n" % item)  
# print(f"excel数据已成功转存到txt {txt_file_path}")


# # #####--------------------transfer excel to json-------------------------------
# import pandas as pd  
# import json  
  
# # Excel文件路径  
# excel_file_path = r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\wiki_info.csv'  
# # 指定列的列名  
# column_name = 'abs'  # 假设你要提取的是第3列，列名为'Column3'  
# # 使用pandas读取CSV文件（注意这里是CSV文件，不是Excel文件）  
# df = pd.read_csv(excel_file_path, usecols=[column_name])  
# # 提取指定列的数据  
# data = df[column_name].tolist()  
# # 将数据转换为JSON格式  
# json_data = json.dumps(data, ensure_ascii=False, indent=4)  # indent用于格式化输出，使其更易读  
# # JSON文件路径  
# json_file_path = r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\wiki_info.json'  
  
# # 将JSON数据写入文件  
# with open(json_file_path, 'w', encoding='utf-8') as f:  
#     f.write(json_data)  
  
# print(f"excel数据已成功转存到json {json_file_path}")


# # # # ##-------------------去除文本中的标点等--------------------------------
# import re,string  
# import numpy as np
# def remove_punctuation(text):  
#     # 创建一个转换表，其中包含所有要删除的字符及其对应的删除字符（None）  
#     translator = str.maketrans('', '', string.punctuation + '#@￥&%')  
#     # 使用转换表来翻译（即删除）文本中的标点符号  
#     return text.translate(translator)  
# dic,pattern,Lst={},'[^\u4e00-\u9fa5]',[]
# with open('.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\wiki_info_无标点等.txt', 'a', encoding='utf-8') as outFile:  
#     # 使用'with'语句来打开文件，这样可以确保文件在读取完毕后被正确关闭  
#     with open(r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\wiki_info.txt', 'r', encoding='utf-8') as infile:  
#         # 使用for循环逐行读取文件  
#         for line in infile:  
#             # 处理每一行，这里只是简单地打印出来  
#             text=remove_punctuation(line)#re.sub(pattern, '', line) #去除标点符号，#等
#             Lst.append(text)
#             outFile.write(text)



# # ##-------------------pdf转txt方法1--------------------------------
# import pdfplumber,re  
# # PDF文件路径  
# pdf_path = r'.\通用规范汉字表.pdf'
# dic,pattern={},'[^\u4e00-\u9fa5]'
# # 打开PDF文件  
# with pdfplumber.open(pdf_path) as pdf:  
#     # 遍历PDF中的每一页  
#     for page in pdf.pages:  
#         # 提取页面的文本  
#         text = page.extract_text()  
#         text=re.sub(r'\d+', '', text)
#         # text=text.replace('\n','')
#         text=text.strip()
#         text=re.sub(pattern, '', text) #去除标点符号，#等。
#         # 将文本写入TXT文件（这里假设每一页都写入同一个文件）  
#         with open('./dataTokenCls_SentencenSegmentation/data/0323vocab通用词汇表/通用规范汉字表.txt', 'a', encoding='utf-8') as f:  
#             for char in text:  
#                 if char.__contains__(' '):
#                     continue
#                 if char.strip():  # 去除空白字符  
#                     f.write(char + '\n')
#                     if char not in  dic.keys():
#                         dic[char]=1
# print(len(dic.keys())  )                  
# print("OK")


# # ##-------------------pdf转txt方法2--------------------------------
# # from pdfminer.high_level import extract_text  
# # # PDF文件路径  
# # pdf_path = r'.\通用规范汉字表.pdf'
# # # 提取PDF中的文本  
# # text = extract_text(pdf_path)  
# # text=text.replace('\n','')  
# # text=text.strip()
# # # 将文本写入TXT文件  
# # with open('./dataTokenCls_SentencenSegmentation/data/0323vocab通用词汇表/output0323.txt', 'w', encoding='utf-8') as f:  
# #     f.write(text)


# # ##-------------------获取shp中字段值的中位数、1/3位数--------------------------------
import geopandas as gpd  
import numpy as np  
import os  
# 假设所有的shapefiles都在同一个目录下  
shp_directory = r'G:\BT\data\1lineUnit'  
outTxt=r'G:\BT\data\2corpus\1ClsSection30个市0520.txt'
#   # 使用glob模块找到目录下所有的shapefiles  
# shp_files = [
#              shp_directory+'\Split257_2Yulin_DelLineUnit.shp',
#              shp_directory+'\Split257_2Yanan_DelLineUnit.shp',
#              shp_directory+'\Split257_2Weinan_DelLineUnit.shp',
#              shp_directory+'\Split257_2BaojiLineUnit.shp',
             
#              shp_directory+'\Split257_QingyangLineUnit.shp',
#              shp_directory+'\Split257_BaiyinLineUnit.shp',
#              shp_directory+'\Split257_PingliangLineUnit.shp',
#              shp_directory+'\Split257_YunchengLineUnit.shp',
             
#             #  shp_directory+'\Split257_2Tongchuan_DelLineUnit.shp',
#             #  shp_directory+'\Split257_XianyangLineUnit.shp',

#              ]  

# 初始化一个空列表来存储所有的len值  
lengths = []  
corner_value =[]  
slope_value=[]  
sum_len=[]  

GSCDLen1=[]  
GSCDLen2=[]  
GSCDLen3=[]  
GSCDLen4=[]  
GSCDLen5=[]  
GSCDLen6=[]  
# # 遍历所有的shapefiles  
# for shp_file in shp_files:  
# 遍历目录下的所有条目
for shp_file in os.listdir(shp_directory):
    # 检查条目是否为文件而非目录
    if os.path.isfile(os.path.join(shp_directory, shp_file)) and shp_file.endswith('.shp'):
        # 读取shapefile  
        gdf = gpd.read_file(shp_directory+'/'+shp_file)  
        
        # 检查'len'字段是否存在  
        if 'len' in gdf.columns and 'corner' in gdf.columns and 'slope' in gdf.columns and 'len_Sum' in gdf.columns and 'GSCDLen1' in gdf.columns and 'GSCDLen2' in gdf.columns and 'GSCDLen3' in gdf.columns and 'GSCDLen4' in gdf.columns and 'GSCDLen5' in gdf.columns and 'GSCDLen6' in gdf.columns:  
            # 将'len'字段的值添加到列表中  
            lengths.extend(gdf['len'].tolist())  
            corner_value.extend(gdf['corner'].tolist())  
            slope_value.extend(gdf['slope'].tolist())  
            sum_len.extend(gdf['len_Sum'].tolist())  
            GSCDLen1.extend(gdf['GSCDLen1'].tolist())  
            GSCDLen2.extend(gdf['GSCDLen2'].tolist())  
            GSCDLen3.extend(gdf['GSCDLen3'].tolist())  
            GSCDLen4.extend(gdf['GSCDLen4'].tolist())  
            GSCDLen5.extend(gdf['GSCDLen5'].tolist())  
            GSCDLen6.extend(gdf['GSCDLen6'].tolist())  
        else:  
            if 'len' not in gdf.columns:
                print(f"The field 'len' does not exist in {shp_file}")  
            if 'corner' not in gdf.columns:
                print(f"The field 'corner' does not exist in {shp_file}")  
            if 'slope' not in gdf.columns:
                print(f"The field 'slope' does not exist in {shp_file}")    
            if 'len_Sum' in gdf.columns:
                print(f"The field 'len_Sum' does not exist in {shp_file}")                            
                
            if 'GSCDLen1' not in gdf.columns:
                print(f"The field 'GSCDLen1' does not exist in {shp_file}")    
            if 'GSCDLen2' not in gdf.columns:
                print(f"The field 'GSCDLen2' does not exist in {shp_file}")    
            if 'GSCDLen3' not in gdf.columns:
                print(f"The field 'GSCDLen3' does not exist in {shp_file}")    
            if 'GSCDLen4' not in gdf.columns:
                print(f"The field 'GSCDLen4' does not exist in {shp_file}")    
            if 'GSCDLen5' not in gdf.columns:
                print(f"The field 'GSCDLen5' does not exist in {shp_file}")    
            if 'GSCDLen6' not in gdf.columns:
                print(f"The field 'GSCDLen6' does not exist in {shp_file}")                                                                            
Value1_3=33.3
Value2_3=66.7
# 打开文件以写入内容。如果文件不存在，它将被创建。如果文件存在，它的内容将被覆盖。  
with open(outTxt, 'w', encoding='utf-8') as f:  
    # 计算合并后的列表的区间值  
    #1.length
    # median = np.median(lengths)  
    q1 = np.percentile(lengths, Value1_3)  
    q3 = np.percentile(lengths, Value2_3)  
    # f.write(f"Median of lengths: {median}")            
    f.write(f"1/3 of lengths: {q1}\n")
    f.write(f"2/3 of lengths: {q3}\n")
    # 输出结果  
    # print(f"Median of lengths: {median}")  
    print(f"1/3 of lengths: {q1}")  
    print(f"2/3 of lengths: {q3}")   
    
    #2.corner 
    # median = np.median(corner_value)  
    q1 = np.percentile(corner_value, Value1_3)  
    q3 = np.percentile(corner_value, Value2_3)      
    # f.write(f"Median of corner_value: {median}")            
    f.write(f"1/3 of corner_value: {q1}\n")
    f.write(f"2/3 of corner_value: {q3}\n")
    # 输出结果  
    # print(f"Median of corner_value: {median}")  
    print(f"1/3 of corner_value: {q1}")  
    print(f"2/3 of corner_value: {q3}")
    
     #3.slope
    # median = np.median(slope_value)  
    q1 = np.percentile(slope_value, Value1_3)  
    q3 = np.percentile(slope_value, Value2_3)      
    # f.write(f"Median of slope_value: {median}")            
    f.write(f"1/3 of slope_value: {q1}\n")
    f.write(f"2/3 of slope_value: {q3}\n")
    # 输出结果  
    # print(f"Median of slope_value: {median}")  
    print(f"1/3 of slope_value: {q1}")  
    print(f"2/3 of slope_value: {q3}")    
    
     #4.sum_len
    # median = np.median(sum_len)  
    q1 = np.percentile(sum_len, Value1_3)  
    q3 = np.percentile(sum_len, Value2_3)      
    # f.write(f"Median of sum_len: {median}")            
    f.write(f"1/3 of sum_len: {q1}\n")
    f.write(f"2/3 of sum_len: {q3}\n")
    # 输出结果  
    # print(f"Median of sum_len: {median}")  
    print(f"1/3 of sum_len: {q1}")  
    print(f"2/3 of sum_len: {q3}")    
    
    
     #5.GSCDLen1
    median = np.median(GSCDLen1)  
    # q1 = np.percentile(GSCDLen1, Value1_3)  
    # q3 = np.percentile(GSCDLen1, Value2_3)      
    f.write(f"Median of GSCDLen1: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen1: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen1: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen1: {median}\n")  
    # print(f"First Quartile (Q1) of GSCDLen1: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen1: {q3}")      
    
     #6.GSCDLen2
    median = np.median(GSCDLen2)  
    # q1 = np.percentile(GSCDLen2, Value1_3)  
    # q3 = np.percentile(GSCDLen2, Value2_3)      
    f.write(f"Median of GSCDLen2: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen2: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen2: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen2: {median}")  
    # print(f"First Quartile (Q1) of GSCDLen2: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen2: {q3}")      
    
     #7.GSCDLen3
    median = np.median(GSCDLen3)  
    # q1 = np.percentile(GSCDLen3, Value1_3)  
    # q3 = np.percentile(GSCDLen3, Value2_3)      
    f.write(f"Median of GSCDLen3: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen3: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen3: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen3: {median}\n")  
    # print(f"First Quartile (Q1) of GSCDLen3: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen3: {q3}")      
    
     #8.GSCDLen4
    median = np.median(GSCDLen4)  
    # q1 = np.percentile(GSCDLen4, Value1_3)  
    # q3 = np.percentile(GSCDLen4, Value2_3)      
    f.write(f"Median of GSCDLen4: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen4: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen4: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen4: {median}")  
    # print(f"First Quartile (Q1) of GSCDLen4: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen4: {q3}")      
    
     #9.GSCDLen5
    median = np.median(GSCDLen5)  
    # q1 = np.percentile(GSCDLen5, Value1_3)  
    # q3 = np.percentile(GSCDLen5, Value2_3)      
    f.write(f"Median of GSCDLen5: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen5: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen5: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen5: {median}")  
    # print(f"First Quartile (Q1) of GSCDLen5: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen5: {q3}")      
    
     #10.GSCDLen6
    median = np.median(GSCDLen6)  
    # q1 = np.percentile(GSCDLen6, Value1_3)  
    # q3 = np.percentile(GSCDLen6, Value2_3)      
    f.write(f"Median of GSCDLen6: {median}\n")            
    # f.write(f"First Quartile (Q1) of GSCDLen6: {q1}")
    # f.write(f"Third Quartile (Q3) of GSCDLen6: {q3}")
    # 输出结果  
    print(f"Median of GSCDLen6: {median}")  
    # print(f"First Quartile (Q1) of GSCDLen6: {q1}")  
    # print(f"Third Quartile (Q3) of GSCDLen6: {q3}")      


# # # # ------------------------线元质心为图节点，构建DT,构建三角网---------------------------
# import numpy as np
# from scipy.spatial import Delaunay
# import geopandas as gpd
# from shapely.geometry import LineString

# # 读取点数据
# point_shp_path = r'G:\研究\博士答辩\2开题\图片\数据\构图的等高线线元中点_1个地形单元.shp'
# gdf = gpd.read_file(point_shp_path)

# # 提取点坐标
# points = np.column_stack((gdf.geometry.x, gdf.geometry.y))

# # 构建 Delaunay 三角网
# tri = Delaunay(points)

# # 提取三角网的边
# edges = set()
# for simplex in tri.simplices:
#     simplex = np.sort(simplex)
#     edges.update({(simplex[0], simplex[1]), (simplex[0], simplex[2]), (simplex[1], simplex[2])})

# # 创建 GeoDataFrame 存储边
# lines = []
# for i, (p1, p2) in enumerate(edges):
#     line = LineString([tuple(points[p1]), tuple(points[p2])])
#     lines.append((i, line))

# lines_gdf = gpd.GeoDataFrame(lines, columns=['ID', 'geometry'])

# # 保存边为线 shapefile
# line_shp_path =r"G:\研究\博士答辩\2开题\图片\数据\tin_edge.shp', driver='ESRI Shapefile"
# lines_gdf.to_file(line_shp_path)

# print("Delaunay 三角网的边已保存到", line_shp_path)

# w='w'
# n_cur=1
# num_word=5184
# outPath_vocab=r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabContour0512.txt'
# with open(outPath_vocab, 'w', encoding='utf-8') as f:  
#     for i in range(5184):
#         f.write(w+str(n_cur))
#         f.write('\n')
#         n_cur=n_cur+1
# print("完成写入vocabContour！")        



# Vocab_Dic,Vocab_DicContoutW,Map_Two_Vocab={},{},{}
# outVocab_Dic=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen.txt'
# outVocab_DicContoutW=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen_ContourW0512.txt'
# Dic_MapTwoVocab=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_MapTwoVocab0512.txt'
# import numpy as np
# vocabLst = np.loadtxt(outVocab_Dic, dtype=str, encoding='utf-8',delimiter='\t')
# vocab_contourLst = np.loadtxt(outVocab_DicContoutW, dtype=str, encoding='utf-8',delimiter='\t')

# for i in range(len(vocabLst)):
#     k,v=vocabLst[i][0],vocabLst[i][1]
#     if k not in Vocab_Dic.keys():
#         Vocab_Dic[k]=v
# for i in range(len(vocab_contourLst)):
#     k,v=vocab_contourLst[i][0],vocab_contourLst[i][1]
#     if k not in Vocab_DicContoutW.keys():
#         Vocab_DicContoutW[k]=v        
# with open(Dic_MapTwoVocab, 'w', encoding='utf-8') as f:  
#     for k in Vocab_Dic.keys():
#         if k not in Map_Two_Vocab.keys():
#             Map_Two_Vocab[Vocab_Dic[k]]=Vocab_DicContoutW[k]
# #         s= Vocab_Dic[k]  +'\t'+Vocab_DicContoutW[k]
# #         f.write(s+'\n')
# # print('完成')        
# directory_lst=[r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\corpus128_4个市0411',r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\corpus128_8个市0416']
# out_directory=r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\corpus128_0512'
# for dd_i in range(len(directory_lst)):
#     directory=directory_lst[dd_i]
#     # 遍历目标目录及其所有子目录  
#     for root, dirs, files in os.walk(directory):  
#         for file in files:  
#             if not file.endswith(".txt"):
#                 print(file)
#                 continue
#             oldCorpusPath=os.path.join(root, file) 
#             newCorpusPath=os.path.join(out_directory, file)

#             Corpus_1line=[]
#             with open(oldCorpusPath, 'r', encoding='utf-8') as f:  
#                 for line in f:  
#                     content = line.strip('\n').split(' ')  
#                     for i in range(len(content)):
#                         Corpus_1line.append(Map_Two_Vocab[content[i]])
#                     with open(newCorpusPath, 'a', encoding='utf-8') as result_file:  
#                         list_str = ' '.join(Corpus_1line)   
#                         result_file.writelines(f"{list_str}\n")   
#                         Corpus_1line=[]                          
#             print('已完成转换语料库：'+ os.path.basename(oldCorpusPath))

