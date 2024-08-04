

import geopandas as gpd  
from shapely.geometry import mapping, shape  
from pyproj import CRS, Transformer   
#---------define  shp  to target spatial reference---------------------------------------------------
def DefineOneShpSpatialReference(file_path,spatialReference,out_file_path):
    # 读取shapefile  
    gdf = gpd.read_file(file_path)  
      
    # 如果GeoDataFrame没有CRS信息或者CRS不是WGS 84 Web Mercator，则设置它  
    if gdf.crs is None or gdf.crs.to_string() != spatialReference.to_string():  
        gdf.crs = spatialReference  
    
    # 保存转换后的shapefile（如果需要）  
    # 假设您想要保留原始文件名，只需将'your_file_transformed.shp'替换为转换后的文件名  
    gdf.to_file(out_file_path, driver='ESRI Shapefile')  
    
### ---------define every shp in the directory to target spatial reference------------------------------------------------------------
def DefineShpsSpatialReference(directory, spatialReference,outDirectory):
    # 确保输出目录存在  
    if not os.path.exists(outDirectory):  
        os.makedirs(outDirectory)  
  
    # 遍历目标目录及其所有子目录  
    for root, dirs, files in os.walk(directory):  
        # 构造输出目录的对应路径  
        relative_path = os.path.relpath(root, directory)  
        out_path = os.path.join(outDirectory, relative_path)  
  
        # 如果输出路径的目录不存在，则创建它  
        if not os.path.exists(out_path):  
            os.makedirs(out_path)  
  
        # 处理并复制文件  
        for file in files:  
            if file.endswith(".shp"):
                file_path = os.path.join(root, file)  
                out_file_path = os.path.join(out_path, file)  
                DefineOneShpSpatialReference(file_path,spatialReference,out_file_path) 
                
                            
    print("complete define ")

##---------------分割线shp：每隔一定点数pntNum分割线.  输出 分割后的线shp-----------------------------------------------
import os  
import geopandas as gpd  
from shapely.geometry import LineString  
# 定义一个函数来提取数字并转换为字符串  
def extract_number(value):  
    if isinstance(value, str) and '.' in value:  
        # 去除单位'm'并转换为浮点数，然后转换为整数（如果需要的话）  
        # 如果elevation字段本身就是整数，可以省略float()转换  
        number =value.split('.')[0]  
        # 如果需要整数形式  
        # number = int(number)  
        return str(number)  # 转换为字符串  
    elif isinstance(value, str) and ' ' in value: 
        number =value.split(' ')[0]  
        # 如果需要整数形式  
        # number = int(number)  
        return str(number)  # 转换为字符串
    else: 
        return None  # 或者你可以返回一个默认值或处理错误情况  
  
# 应用函数到'elevation'字段，并创建新的'Contour'字段  
def SplitLineByPntNum(pntNum,input_directory,file_name,ouput_directory):  
    shpPath=os.path.join(input_directory,file_name)
    # 加载原始的线shp文件  
    gdf = gpd.read_file(shpPath)  
    # 检查GeoDataFrame中是否存在'ContourID'字段  
    if 'ContourID' not in gdf.columns:  
        gdf['ContourID'] = gdf.index
        # 将修改后的GeoDataFrame保存回shapefile  
        gdf.to_file(shpPath, driver='ESRI Shapefile')
    if 'Contour' not in gdf.columns:  
        gdf['Contour'] = gdf['ELEVATION'].apply(extract_number)    
        # 将修改后的GeoDataFrame保存回shapefile  
        gdf.to_file(shpPath, driver='ESRI Shapefile')    
    # 初始化一个新的GeoDataFrame来存储截断后的线  
    new_gdf = gpd.GeoDataFrame(columns=gdf.columns)  # 确保新GeoDataFrame的列与原始GDF相同  
      
    directory_path = os.path.dirname(shpPath)  
    file_name = os.path.basename(shpPath)  
    resLinePath = os.path.join(ouput_directory, "Split" + str(pntNum) + "_" + file_name)  
      
    # 遍历每条线  
    for index, row in gdf.iterrows():  
        # 获取线的坐标列表  
        coords = row.geometry.coords[:]  
        count = len(coords)  
          
        # 初始化一个空的坐标列表来存储截断后的线段坐标  
        truncated_coords_list = []  
          
        # 遍历每个坐标点  
        for i, coord in enumerate(coords):  
            # 添加坐标点到当前线段坐标列表  
            truncated_coords_list.append(coord)  
              
            # 如果坐标点数量达到 pntNum 或者遍历到最后一个坐标点  
            if len(truncated_coords_list) == pntNum or i == (count - 1):  
                # 将当前线段坐标转换为LineString  
                truncated_line = LineString(truncated_coords_list)  
                  
                # 创建一个新的GeoSeries  
                truncated_gseries = gpd.GeoSeries([truncated_line])  
                  
                # 创建一个新的GeoDataFrame来存储截断后的线段及其属性  
                truncated_gdf = gpd.GeoDataFrame(geometry=truncated_gseries)  
                  
                # 拷贝其他非几何列的值到新的GeoDataFrame  
                for col in gdf.columns:  
                    if col != 'geometry':  
                        truncated_gdf[col] = row[col]  # 使用当前行的属性值  
                  
                # 将截断后的线段及其属性添加到总的GeoDataFrame中  
                new_gdf = new_gdf.append(truncated_gdf, ignore_index=True)  
                  
                # 重置当前线段的坐标列表  
                truncated_coords_list = [coord]  
      
    # 设置新的GeoDataFrame的CRS  
    new_gdf.crs = gdf.crs  
      
    # 将新的GeoDataFrame保存到新的shp文件中  
    new_gdf.to_file(resLinePath, driver='ESRI Shapefile')  
    print("截断后的线已保存到文件中"+resLinePath)  


# ##----------------------转换目录下所有shp的坐标系----------------------
# # standShpPath=r'G:\研究\BT\图片\2extractFeature\测试转换坐标系\WGS_1984_Web_Mercator_Auxiliary_Sphere.shp' 
# # WGS_1984_Web_Mercator_Auxiliary_Sphere=gpd.read_file(standShpPath).crs
# directory=r'G:\BT\data\0datasource\0319廖心宇'    
# spatialReference = CRS.from_string("EPSG:3857")  
# outDirectory=r'G:\BT\data\0datasource\0319廖心宇转换坐标系'    
# DefineShpsSpatialReference(directory,spatialReference,outDirectory) 

##-------------------分割线，每隔一定点数---------------------
splitPntNum=255#宝鸡进行了每个句子最多254个线元，在BERT中会在开头结尾加上[Cls].[Sep]
input_directory=r'G:\BT\data\0datasource\0rawData\3Del500m'  #r'G:\BT\data\0datasource\0rawData\4ClipXian'
file_name=r'YanAn.shp'
ouput_directory=r'G:\BT\data\0datasource\1simSplitData'
SplitLineByPntNum(splitPntNum,input_directory,file_name,ouput_directory)
