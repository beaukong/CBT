import geopandas as gpd  
import os  
import numpy as np
import json
# #根据线的字段的值，分类线。将分类结果记录到线shp的字段中 
def get_category_label(len_value, corner_value, slope_value, sum_len, GSCDLen1,GSCDLen2,GSCDLen3, GSCDLen4,GSCDLen5,GSCDLen6,
                        len_bins, corner_bins,slope_bins,sum_len_bins,GSCDLen1_bins,GSCDLen2_bins,GSCDLen3_bins,GSCDLen4_bins,GSCDLen5_bins,GSCDLen6_bins):  
    # 获取len字段的类别索引  
    len_category = next(i for i, v in enumerate(len_bins) if len_value < v)  
    # 获取corner字段的类别索引  
    corner_category = next(i for i, v in enumerate(corner_bins) if corner_value < v)  
    # 获取slope字段的类别索引  
    slope_category = next(i for i, v in enumerate(slope_bins) if slope_value < v)      
    
    # 获取sum_len字段的类别索引  
    sum_len_category = next(i for i, v in enumerate(sum_len_bins) if sum_len < v)      
   
    # 获取 GSCDLen1_category 字段的类别索引  
    GSCDLen1_category = next(i for i, v in enumerate(GSCDLen1_bins) if GSCDLen1 < v)      
    # 获取 GSCDLen2_category 字段的类别索引  
    GSCDLen2_category = next(i for i, v in enumerate(GSCDLen2_bins) if GSCDLen2 < v)      
    # 获取 GSCDLen3_category 字段的类别索引  
    GSCDLen3_category = next(i for i, v in enumerate(GSCDLen3_bins) if GSCDLen3 < v)      
    # 获取 GSCDLen4_category 字段的类别索引  
    GSCDLen4_category = next(i for i, v in enumerate(GSCDLen4_bins) if GSCDLen4 < v)      
    # 获取 GSCDLen5_category 字段的类别索引  
    GSCDLen5_category = next(i for i, v in enumerate(GSCDLen5_bins) if GSCDLen5 < v)      
    # 获取 GSCDLen6_category 字段的类别索引  
    GSCDLen6_category = next(i for i, v in enumerate(GSCDLen6_bins) if GSCDLen6 < v)   
    
    # 计算总的类别标签（1-based index）  
    category_label =('len'+str(len_category)+'_'+'corner'+str(corner_category)+'_'+'slope'+str(slope_category)+'_'+'sumlen'+str(sum_len_category)+'_'+
    'GSCDLenOne'+str(GSCDLen1_category)+'_'+'GSCDLenTwo'+str(GSCDLen2_category)+'_'+'GSCDLenThree'+str(GSCDLen3_category)+'_'+
    'GSCDLenFour'+str(GSCDLen4_category)+'_'+'GSCDLenFive'+str(GSCDLen5_category)+'_'+'GSCDLenSix'+str(GSCDLen6_category)
    )

    return category_label  

####用到了3环长度信息熵0324
def ConstructLineUnitCls_Using3entropy_Vocab_Dic(vocab_txt,outVocab_Dic,outDicfile):
    lst_len=['len1','len2','len3','len4']
    lst_corner=['corner1','corner2','corner3','corner4']
    lst_slpoe=['slope1','slope2','slope3','slope4']
    lst_sumlen=['sumlen1','sumlen2','sumlen3']
    lst_entropy1=['entropyOne1','entropyOne2','entropyOne3']
    lst_entropy2=['entropyTwo1','entropyTwo2','entropyTwo3']
    lst_entropy3=['entropyThree1','entropyThree2','entropyThree3'] 
    dic_lineUnitCls_Word,num={},5
    vocab=np.loadtxt(vocab_txt,dtype=str)
    # with open(r'.\vocab0323.txt', 'a', encoding='utf-8') as f:  
    for i in range(len(lst_len)):
        for j in range(len(lst_corner)):
            for k in range(len(lst_slpoe)):
                for l in range(len(lst_sumlen)):
                    for m in range(len(lst_entropy1)):
                        for n in range(len(lst_entropy2)):
                            for o in range(len(lst_entropy3)):
                                cls=lst_len[i]+'_'+lst_corner[j]   +'_' +lst_slpoe[k]  +'_' +lst_sumlen[l]  +'_' +lst_entropy1[m]  +'_' +lst_entropy2[n]  +'_'+lst_entropy3[o]
                                # f.write(cls + '\n')
                                if cls not in dic_lineUnitCls_Word.keys():
                                    dic_lineUnitCls_Word[cls]=vocab[num]
                                    num+=1
    with open(outDicfile, "w") as file:  
        json.dump(dic_lineUnitCls_Word, file)
    # 打开文件，准备写入  
    with open(outVocab_Dic, 'w', encoding='utf-8') as file:  
        # 遍历字典的键值对，并将它们写入文件，每个键值对占一行  
        for key, value in dic_lineUnitCls_Word.items():  
            file.write(f"{key}\t{value}\n")  # 使用制表符'\t'作为键值对之间的分隔符，然后换行  

####用到了1环长度0326
def ConstructLineUnitCls_Using1GSCD_Vocab_Dic(vocab_txt,outVocab_Dic,outDicfile):
    lst_len=['len1','len2','len3']#,'len4']
    lst_corner=['corner1','corner2','corner3']#,'corner4']
    lst_slpoe=['slope1','slope2','slope3']#,'slope4']
    lst_sumlen=['sumlen1','sumlen2','sumlen3']
    lst_GSCDLen1=['GSCDLenOne1','GSCDLenOne2']
    lst_GSCDLen2=['GSCDLenTwo1','GSCDLenTwo2']
    lst_GSCDLen3=['GSCDLenThree1','GSCDLenThree2']
    lst_GSCDLen4=['GSCDLenFour1','GSCDLenFour2']
    lst_GSCDLen5=['GSCDLenFive1','GSCDLenFive2']
    lst_GSCDLen6=['GSCDLenSix1','GSCDLenSix2']

    dic_lineUnitCls_Word,num={},0
    vocab=np.loadtxt(vocab_txt,dtype=str)
    # with open(r'.\vocab0323.txt', 'a', encoding='utf-8') as f:  
    for i in range(len(lst_len)):
        for j in range(len(lst_corner)):
            for k in range(len(lst_slpoe)):
                for l in range(len(lst_sumlen)):
                    for m in range(len(lst_GSCDLen1)):
                        for n in range(len(lst_GSCDLen2)):
                            for o in range(len(lst_GSCDLen3)):
                                for p in range(len(lst_GSCDLen4)):
                                    for q in range(len(lst_GSCDLen5)):
                                        for r in range(len(lst_GSCDLen6)):
                                            cls=(lst_len[i]+'_'+lst_corner[j]   +'_' +lst_slpoe[k]  +'_' +lst_sumlen[l]  +'_' +lst_GSCDLen1[m]  
                                                 + '_' +lst_GSCDLen2[n]  +'_'+lst_GSCDLen3[o]+'_'+ lst_GSCDLen4[p]  +'_' +lst_GSCDLen5[q]  +'_'+lst_GSCDLen6[r])
                                            # f.write(cls + '\n')
                                            if cls not in dic_lineUnitCls_Word.keys():
                                                dic_lineUnitCls_Word[cls]=vocab[num]
                                                num+=1
    with open(outDicfile, "w") as file:  
        json.dump(dic_lineUnitCls_Word, file)
    # 打开文件，准备写入  
    with open(outVocab_Dic, 'w', encoding='utf-8') as file:  
        # 遍历字典的键值对，并将它们写入文件，每个键值对占一行  
        for key, value in dic_lineUnitCls_Word.items():  
            file.write(f"{key}\t{value}\n")  # 使用制表符'\t'作为键值对之间的分隔符，然后换行  
    print('已完成映射线元类别与单词')
# 现在有一个线shp和一个词汇表txt。线shp中存在多个线要素具有相同的
# 建立一个列表Lst，存储词汇表txt中每行的内容。
# 建立一个空字典，和空列表oneSmpleLst
# 遍历线shp中要素，读取其vocab字段和oContourID字段，以vocab字段的值作为字典的key，以Lst的一个要素作为value,并将value添加到oneSmpleLst中；
# 遍历到下一个线要素时，如果其vocab字段的值是新值，则作为key添加到字典中，此时以Lst中下一个要素作为value。
# 当oneSmpleLst有 sampleLen 个要素或者ContourID与上一个线要素的ContourID不同时，则将oneSmpleLst的内容输出到结果txt中，并将oneSmpleLst置空。请给出python代码
def ConstructCorpusByMappingVocabu(vocabPath,LineUnitPath,outCorpusPath, sampleLen):
    vocab_dict={}
    with open(vocabPath, "r") as file:  
        vocab_dict = json.load(file)  
    # # 读取词汇表txt文件到列表Lst  
    # # with open('词汇表.txt', 'r', encoding='utf-8') as vocab_file:  
    # #     vocabLst = [line.strip() for line in vocab_file]  
    # vocabLst = np.loadtxt(vocabPath, dtype=str, encoding='utf-8')
    # # 初始化空字典和空列表  
    # vocab_dict = {}  
    oneSmpleLst = ''  
    # index_vocab=5#前几行是[PAD],[MASK]等
    # 读取线shp文件  
    gdf = gpd.read_file(LineUnitPath)  
    
    # 初始化一个变量来跟踪上一个ContourID  
    prev_contour_id = None  
    
    # 遍历线shp中的每个要素  
    for index, row in gdf.iterrows():  
        vocab = row['vocab_cls']  # 假设vocab_clsl字段在属性表中存在  
        contour_id = row['ContourID']  # 假设ContourID字段在属性表中存在  
        # 如果遍历到下一ContourID的线，将oneSmpleLst中存储的语料序列存储到 txt
        if contour_id != prev_contour_id and prev_contour_id is not None and len(oneSmpleLst)>0:
            with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
                # for item in oneSmpleLst:  
                result_file.write(f"{oneSmpleLst}\n")  
            # 清空oneSmpleLst列表  
            if vocab not in vocab_dict:            
                print(gdf['TagID'])
                # vocab_dict[vocab]=vocabLst[index_vocab]
                # index_vocab=index_vocab+1                
                # oneSmpleLst = vocab_dict[vocab]  
            else:
                oneSmpleLst += vocab_dict[vocab]  
        # 如果oneSmpleLst的长度超过 sampleLen ，则输出,  
        if len(oneSmpleLst) >= sampleLen:  
            with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
                # for item in oneSmpleLst:  
                result_file.write(f"{oneSmpleLst}\n")  
            if vocab not in vocab_dict:            
                print(gdf['TagID'])
            else:
                oneSmpleLst += vocab_dict[vocab]          
        # 如果vocab_clsl是新值
        if vocab not in vocab_dict:
            print(gdf['TagID'])
        else:
            oneSmpleLst+=vocab_dict[vocab]
            
    # 遍历结束后，如果oneSmpleLst还有剩余，则输出到结果txt文件  
    if oneSmpleLst:  
        with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
            # for item in oneSmpleLst:  
            result_file.write(f"{oneSmpleLst}\n")  
    
    print("语料库构建完成，结果已输出。")   

  
# # ##-------------------构建线元类别体系和单词映射字典--------------------------------
# vocab_txt=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabContourW0512.txt'
# outVocab_Dic=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen_ContourW0512.txt'
# outDicfile=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen_ContourW0512.json'
# ConstructLineUnitCls_Using1GSCD_Vocab_Dic(vocab_txt,outVocab_Dic,outDicfile)




# # ##-------------------分类线元、获得单词、语料库--------------------------------
# # 原始的线shp文件  
# # shpPath= r'G:\BT\data\1lineUnit\Split257_YunchengLineUnit.shp'
# #线元类别与单词的映射字典
# inVocab_Dic=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen_ContourW0512.json'
# inShpDirectory=r'G:\BT\data\1lineUnit\LineUnit0606'
# outClassiedShpDirectory=r'G:\BT\data\1lineUnit\ClassifiedLineUnit0606'
# outCorpusDirectory=r'G:\BT\program\ContourBERT\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\corpus126_0606'
# sampleLen=126#0520之后换成126，这是考虑到BERT中会在句子2头添加标记词，对获取地形单元相关等高线的嵌入也有影响：位于2头的词找不到啦。
# # 遍历目标目录及其所有子目录  
# for root, dirs, files in os.walk(inShpDirectory):  
#     for file in files:  
#         if not file.endswith(".shp"):
#             print(file)
#             continue
#         # file_name = os.path.basename(shpPath)  
#         # file_name, _ = os.path.splitext(file_name)
#         file_name, _=os.path.splitext(file)
#         shi_name=file_name.split('_')[1]
#         shi_name_lower=shi_name.lower()
#         shpPath=os.path.join(root, file) 
#         outCorpusPath=os.path.join(outCorpusDirectory, file_name+'.txt')
#         resLinePath = os.path.join(outClassiedShpDirectory, "Classified_"+file_name+".shp")  #(os.path.dirname(shpPath), "Classified_"+file_name+".shp")  
#         if os.path.exists(outCorpusPath): 
#             # 如果文件存在，则删除它  
#             try:  
#                 os.remove(outCorpusPath)  
#                 print(f"文件 {outCorpusPath} 已成功删除。")  
#             except OSError as e:  
#                 print(f"删除文件 {outCorpusPath} 时出错: {e.strerror}") 
#         vocab_dict,oneSmpleLst={},[]
#         with open(inVocab_Dic, "r") as file:  
#             vocab_dict = json.load(file) 
#         gdf = gpd.read_file(shpPath)  
#         # 初始化一个变量来跟踪上一个ContourID  
#         prev_contour_id = gdf.iloc[0]['ContourID']  
#         # 定义len字段的分类区间  
#         len_bins = [0, 128.3054, 250.7087, float('inf')] #右边这是8个市的区间 [0, 94.0688, 209.3850, float('inf')]  #[0, 100, 200, 400, float('inf')]  
#         # 定义corner字段的分类区间  
#         corner_bins = [0, 24.9681, 39.6488, 180]  #[0, 19.5485, 34.7484, 180]  
#         slope_bins=[0,8.3964,13.3776,90]#[0,8.8076,13.89,90]

#         sum_len_bins = [0,  1750.48, 1891.78,float('inf')] #[0, 1770.68, 1908.0,float('inf')] 
#         GSCDLen1_bins=[0,265.46,   float('inf')]#[0, 266.73,   float('inf')]
#         GSCDLen2_bins=[0, 275.98,   float('inf')]#[0, 285.92,   float('inf')]
#         GSCDLen3_bins=[0, 269.25,   float('inf')]#[0, 272.45,   float('inf')]
#         GSCDLen4_bins=[0, 265.6,   float('inf')]#[0, 266.85,   float('inf')]
#         GSCDLen5_bins=[0, 276.26,   float('inf')]
#         GSCDLen6_bins=[0, 269.48,   float('inf')]#[0, 272.97,   float('inf')]

#         # 初始化一个新的列来存储类别标签  
#         gdf['vocab_cls'] = 0
        
#         # 遍历每条线，根据len和corner字段的值分配类别标签  
#         for index, row in gdf.iterrows():  
#             tagid= row['TagID'].lower()
#             if shi_name_lower not in tagid:
#                 tagID_new=shi_name+tagid
#                 gdf.at[index, 'TagID']=tagID_new
#             len_value = row['len']  
#             corner_value = row['corner']  
#             slope_value=row['slope']
            
#             sum_len=row['len_Sum']
#             GSCDLen1=row['GSCDLen1']#order1_GSCDentropy=row['GSCDentr1']
#             GSCDLen2=row['GSCDLen2']
#             GSCDLen3=row['GSCDLen3']
#             GSCDLen4=row['GSCDLen4']
#             GSCDLen5=row['GSCDLen5']
#             GSCDLen6=row['GSCDLen6']
#             #获取线元的类别
#             category_label = get_category_label(len_value, corner_value, slope_value, sum_len, GSCDLen1,GSCDLen2,GSCDLen3, GSCDLen4,GSCDLen5,GSCDLen6,
#                                                 len_bins, corner_bins,slope_bins,sum_len_bins,GSCDLen1_bins,GSCDLen2_bins,GSCDLen3_bins,GSCDLen4_bins,GSCDLen5_bins,GSCDLen6_bins)  
#             gdf.at[index, 'vocab_cls'] = category_label  
            
#             #获得对应的单词、语料库序列
#             vocab = category_label  
#             contour_id = row['ContourID']  # 假设ContourID字段在属性表中存在  
#             # 如果遍历到下一ContourID的线，将oneSmpleLst中存储的语料序列存储到 txt
#             if contour_id != prev_contour_id and prev_contour_id is not None and len(oneSmpleLst)>0:
#                 with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
#                     list_str = ' '.join(oneSmpleLst) 
#                     result_file.write(f"{list_str}\n")  
#                 oneSmpleLst=[]# 清空oneSmpleLst列表
#                 prev_contour_id=contour_id
#                 if vocab not in vocab_dict:            
#                     print(gdf['TagID'])
#                 else:
#                     oneSmpleLst.append(vocab_dict[vocab])
#                     continue
#             # 如果oneSmpleLst的长度超过 sampleLen ，则输出,  
#             if len(oneSmpleLst) >= sampleLen:  
#                 with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
#                     list_str = ' '.join(oneSmpleLst)   
#                     result_file.write(f"{list_str}\n")  
#                 oneSmpleLst=[]# 清空oneSmpleLst列表
#                 if vocab not in vocab_dict:            
#                     print(row['TagID'])
#                 else:
#                     oneSmpleLst.append(vocab_dict[vocab])  
#                     continue        
#             # 如果vocab_clsl是新值
#             if vocab not in vocab_dict:
#                 print(gdf['TagID'])
#             else:
#                 oneSmpleLst.append(vocab_dict[vocab])
                
#         # 遍历结束后，如果oneSmpleLst还有剩余，则输出到结果txt文件  
#         if oneSmpleLst:  
#             with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
#                 list_str = ' '.join(oneSmpleLst)   
#                 result_file.write(f"{list_str}\n")  
#                 oneSmpleLst=[]# 清空oneSmpleLst列表

#         # 如果需要，可以将更新后的GeoDataFrame保存到新的shp文件中  
#         gdf.to_file(resLinePath, driver='ESRI Shapefile')  
#         print("带有类别标签的线已保存到文件中，生成语料库") 


# ##-------------------对分类过的线元，获得不同长度序列的语料库--------------------------------
inShpDirectory=r'G:\BT\data\3downStreamTask\MorphologicalClustering\2LineUnit汇总4类0606'
outCorpusDirectory=r'G:\BT\data\3downStreamTask\MorphologicalClustering\3Corpus126_0606'
#线元类别与单词的映射字典
inVocab_Dic=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic_GSCDLen_ContourW0512.json'
sampleLen=126
# 遍历目标目录及其所有子目录  
for root, dirs, files in os.walk(inShpDirectory):  
    for file in files:  
        if not file.endswith(".shp"):
            print(file)
            continue
        # file_name = os.path.basename(shpPath)  
        # file_name, _ = os.path.splitext(file_name)
        file_name, _=os.path.splitext(file)
        shpPath=os.path.join(root, file) 
        outCorpusPath=os.path.join(outCorpusDirectory, file_name+'.txt')
        if os.path.exists(outCorpusPath): 
            # 如果文件存在，则删除它  
            try:  
                os.remove(outCorpusPath)  
                print(f"文件 {outCorpusPath} 已成功删除。")  
            except OSError as e:  
                print(f"删除文件 {outCorpusPath} 时出错: {e.strerror}") 
        # if not os.path.exists(outCorpusDirectory):
        #     os.makedirs(outCorpusDirectory)        
        vocab_dict,oneSmpleLst={},[]
        with open(inVocab_Dic, "r") as file:  
            vocab_dict = json.load(file) 
        gdf = gpd.read_file(shpPath)  
        # 初始化一个变量来跟踪上一个ContourID  
        prev_contour_id = gdf.iloc[0]['ContourID']  

        # 遍历每条线，根据len和corner字段的值分配类别标签  
        for index, row in gdf.iterrows():  

            #获得对应的单词、语料库序列
            vocab = row['vocab_cls']#category_label    
            contour_id = row['ContourID']  # 假设ContourID字段在属性表中存在  
            # 如果遍历到下一ContourID的线，将oneSmpleLst中存储的语料序列存储到 txt
            if contour_id != prev_contour_id and prev_contour_id is not None and len(oneSmpleLst)>0:
                with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
                    list_str = ' '.join(oneSmpleLst) 
                    result_file.write(f"{list_str}\n")  
                oneSmpleLst=[]# 清空oneSmpleLst列表
                prev_contour_id=contour_id
                if vocab not in vocab_dict:            
                    print(gdf['TagID'])
                else:
                    oneSmpleLst.append(vocab_dict[vocab])
                    continue
            # 如果oneSmpleLst的长度超过 sampleLen ，则输出,  
            if len(oneSmpleLst) >= sampleLen:  
                with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
                    list_str = ' '.join(oneSmpleLst)   
                    result_file.write(f"{list_str}\n")  
                oneSmpleLst=[]# 清空oneSmpleLst列表
                if vocab not in vocab_dict:            
                    print(row['TagID'])
                else:
                    oneSmpleLst.append(vocab_dict[vocab])  
                    continue        
            # 如果vocab_clsl是新值
            if vocab not in vocab_dict:
                print(gdf['TagID'])
            else:
                oneSmpleLst.append(vocab_dict[vocab])
                
        # 遍历结束后，如果oneSmpleLst还有剩余，则输出到结果txt文件  
        if oneSmpleLst:  
            with open(outCorpusPath, 'a', encoding='utf-8') as result_file:  
                list_str = ' '.join(oneSmpleLst)   
                result_file.write(f"{list_str}\n")  
                oneSmpleLst=[]# 清空oneSmpleLst列表

        # # 如果需要，可以将更新后的GeoDataFrame保存到新的shp文件中  
        # file_name = os.path.basename(shpPath)  
        # file_name, _ = os.path.splitext(file_name)
        # resLinePath = os.path.join(os.path.dirname(shpPath), "Classified_"+file_name+".shp")  
        # gdf.to_file(resLinePath, driver='ESRI Shapefile')  
        print("对分类过的线元，获得不同长度序列的语料库"+file_name) 


# import time  
# time.sleep(2)# 让代码等待2秒 
# # ##-------------------构建语料库[4月不再用了 ]--------------------------------
# LineUnitPath=shpPath#r'G:\BT\data\1lineUnit\Classified_2800测试0324LineUnit.shp'
# inVocab_Dic=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\vocabDic.json'
# outCorpusPath=r'.\dataTokenCls_SentencenSegmentation\data\custom_tokenizer0318\corpus0324_2800测试0324LineUnit.txt'
# sampleLen=256
# ConstructCorpusByMappingVocabu(inVocab_Dic,LineUnitPath,outCorpusPath,sampleLen)     


