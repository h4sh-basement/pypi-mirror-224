from datetime import datetime
from tqdm import tqdm
import weaviate
from weaviate.util import generate_uuid5

from recommend_model_sdk.tools.common_tool import CommonTool
from recommend_model_sdk.tools.model_tool import ModelTool
from recommend_model_sdk.recommend.common_enum import RecommendSupportLanguageEnum,RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT
class WeaviateTool:
    """
    use cloud_id instead relpace url
    """
    def __init__(self,model_root_dir,cloud,cloud_url=None,cloud_api_key=None,private_ip=None,private_port=None) -> None:
        if isinstance(cloud,bool) is False:
            raise ValueError("cloud is not bool")
        if cloud:
            if isinstance(cloud_url,str) is False:
                raise ValueError("url is not str")
            if isinstance(cloud_api_key,str) is False:
                raise ValueError("api_key is not str")
            self.__client = weaviate.Client(url=cloud_url,auth_client_secret=weaviate.AuthApiKey(api_key=cloud_api_key))
        else:
            if isinstance(private_ip,str) is False:
                raise ValueError("private_ip is not str")
            if isinstance(private_port,int) is False:
                raise ValueError("private_port is not int ")
            self.__client = weaviate.Client(url=f'http://{private_ip}:{private_port}')
            
        
        self.__model_tool = ModelTool(model_root_dir)
        self.__common_tool = CommonTool()
        self.__logger = self.__common_tool.get_logger()
        self.__feed_id_to_feed = self.__model_tool.download_latest_all_feed()
        self.__category_name_to_category = self.__model_tool.download_latest_all_category()
        self.__class_properties = set()
        # self.__class_properties.add("url")
        self.__class_properties.add("published_at")
        # self.__class_properties.add("package_id")
        self.__class_properties.add("subdoc_index")
        self.__class_properties.add("first_level_category")
        # self.__class_properties.add("second_level_category")
        self.__class_properties.add("major_language") # not property
        # self.__class_properties.add("keyword_list")
        # self.__class_properties.add("filtered")
        self.__class_properties.add("cloud_id")
        self.__support_language_set = RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT.get_all_lang_detect_language_set()
        
    def get_class_properties(self):
        return self.__class_properties  
    
    def init_class(self,model_name,model_version,ef=None,ef_construction=None,max_connections=None,vector_cache_max_objects=None,metadata=True):
        # text,image,model_name, model_version, include, image, text, video, audio
        # https://weaviate.io/developers/weaviate/config-refs/datatypes weaviate_type
        vector_index_config = dict()
        if ef is not None:
            if isinstance(ef,int) is False:
                raise ValueError("ef is not int")
            if ef < -1:
                raise ValueError("ef should greater than -1")
            vector_index_config["ef"] = ef
            
        if ef_construction is not None:
            if isinstance(ef_construction,int) is False:
                raise ValueError("ef_construction is not int")
            if ef_construction <= 0:
                raise ValueError("ef_construction greater than 0")
            vector_index_config["efConstruction"] = ef_construction
    
            
        if max_connections is not None:
            if isinstance(max_connections,int) is False:
                raise ValueError("max_connections is not int")
            if max_connections <= 0:
                raise ValueError("max_connection should greater than 0")
            vector_index_config["maxConnections"] = max_connections
            
        
        if vector_cache_max_objects is not None:
            if isinstance(vector_cache_max_objects,int) is False:
                raise ValueError("vector_cache_max_objects is not int")
            if vector_cache_max_objects <= 0:
                raise ValueError("vector_cache_max_objects should greater than 0")
            vector_index_config["vectorCacheMaxObjects"] = vector_cache_max_objects
        '''
        class_obj = {
            "class":f'{model_name}_{model_version}',
            'properties':[
                {
                    'name':'url', # for secrete
                    'dataType':['text'],
                },
                {
                    'name':'published_at',
                    'dataType':['date'],
                },
                {
                    'name':'package_id',
                    'dataType':['text'],
                },
                {
                    'name':'subdoc_index',
                    'dataType':['int'], # if subdoc_index is -1, represent it is summary embedding, not subdoc embedding
                },
                {
                    'name':'first_level_category',
                    'dataType':['text'], # category two level, which level
                },
                {
                    'name':'second_level_category',
                    'dataType':['text'], # category second level, which level
                },
                {
                    'name':'major_language',
                    'dataType':['text'],
                },
                {
                    'name':'keyword_list',
                    'dataType':['text[]'],
                },
                {
                    'name':'filtered',
                    'dataType':['boolean']
                },
                {
                    'name':'cloud_id',
                    'dataType':['int']
                }
            ],

        }
        '''
        
        simple_class_properties = [
                {
                    'name':'subdoc_index',
                    'dataType':['int'], # if subdoc_index is -1, represent it is summary embedding, not subdoc embedding
                },
                {
                    'name':'first_level_category',
                    'dataType':['int'], # category two level, which level
                },
                {
                    'name':'published_at',
                    'dataType':['int'],
                },
                {
                    'name':'cloud_id',
                    'dataType':['int']
                }
        ]
        class_obj = dict()
        if metadata is True:
            class_obj["properties"] = simple_class_properties
            
        if len(vector_index_config) > 0:
            class_obj["vectorIndexConfig"] = vector_index_config
            
        for current_language in self.__support_language_set:
            class_name = f'{model_name}_{model_version}_{current_language}'
            class_name = self.make_class_name_valid_name(class_name)
            self.__logger.debug(f'create class {class_name}')
            class_obj['class'] = class_name
            self.__client.schema.create_class(class_obj)
            self.__logger.debug(f'create class {class_name} success')

    
    def delete_class(self,model_name,model_version):
        class_name = f'{model_name}_{model_version}'
        for current_language in self.__support_language_set:
            class_name = f'{model_name}_{model_version}_{current_language}'
            self.__logger.debug(f'delete class {class_name}')
            class_name = self.make_class_name_valid_name(class_name)
            self.__client.schema.delete_class(class_name)  
            self.__logger.debug(f'delete class {class_name} success')
        
    
    def insert_package_data(self,package_info,target_model_name,target_model_version,metadata=True):
        """_summary_

        Args:
            package_info (_type_): _description_
            target_model_name (_type_): _description_
            target_model_version (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
            {
                url:{
                    "success": bool
                    "fail_reason": ["",""], if success if True
                    "cloud_id": int
                    "uuids":{
                        "subdoc": uuid   # subdoc 
                    }
                    
                }
            }
        """
        if isinstance(package_info,dict) is False:
            raise ValueError("package_info is not dict")
        
        if "package_id" not in package_info:
            raise ValueError("package_id is not exist")
        current_pacakge_id = package_info["package_id"]
        if isinstance(current_pacakge_id,str) is False:
            raise ValueError("package_id is not str")
        
        if "model_name" not in package_info:
            raise ValueError("model_name is not exist in package_info")
        current_model_name = package_info["model_name"]
        if isinstance(current_model_name,str) is False:
            raise ValueError("current_model_name is not str")
        
        if "model_version" not in package_info:
            raise ValueError("model_version is not exist in package_info")
        current_model_version = package_info["model_version"]
        if isinstance(current_model_version,str) is False:
            raise ValueError("current_model_version is not str")
        
        if isinstance(target_model_name,str) is False:
            raise ValueError("target_model_name is not str")
        if isinstance(target_model_version,str) is False:
            raise ValueError("target_model_version is not str")
        
        self.__model_tool.valid_model_name_and_version(target_model_name,target_model_version)
        self.__model_tool.valid_model_name_and_version(current_model_name,current_model_version)
        
        if current_model_name != target_model_name:
            self.__logger.debug(f'current_model_name {current_model_name} not equal  current_model_version {current_model_version}')
            return
        
        if current_model_version  != target_model_version:
            self.__logger.debug(f'current_model_version {current_model_version} not equal target_model_version {target_model_version}')
            return
        
        main_language = package_info["main_language"]
        schema_class = f'{current_model_name}_{current_model_version}_{main_language}'
        schema_class = self.make_class_name_valid_name(schema_class)
        self.__logger.debug(f'schema_class {schema_class}')
        
        url_to_article_dict,url_to_embedding_dict = self.__model_tool.download_increment_package(target_model_name,target_model_version,current_pacakge_id)
        self.__logger.debug(f'article length= {len(url_to_article_dict)}')
        url_to_success_info = dict()
        with self.__client.batch(batch_size=100) as batch:
            for current_url, current_article in url_to_article_dict.items():
                url_to_success_info[current_url] = {}
                url_to_success_info[current_url]["success"] = True
                url_to_success_info[current_url]["fail_reasons"] = list()
                temp_property = dict()
                # temp_property["url"] = current_url
                if 'published_at' in current_article and current_article['published_at'] is not None :
                    current_published_at = int(current_article["published_at"])
                    # date_published_at = datetime.fromtimestamp(current_published_at*1.0/1000)
                    # temp_property["published_at"] = date_published_at.strftime("%Y-%m-%dT%H:%M:%SZ")
                    temp_property["published_at"] = current_published_at
                # temp_property["package_id"] = current_pacakge_id
                # temp_property["major_language"] = current_article["major_language"]
                # temp_property['filtered'] = False
                temp_property['cloud_id'] = int(current_article['cloud_id'])
                # if "keyword_list" in temp_property:
                #    temp_property["keyword_list"] = current_article["keyword_list"]
                # print(type(current_article["feed_id"]))
                current_category_name = self.__feed_id_to_feed[int(current_article["feed_id"])]["category_title"]
                current_category_info =  self.__category_name_to_category[current_category_name]
                
                if current_category_info["level"] == "first":
                    # temp_property["first_level_category"] = current_category_info["category"]
                    temp_property["first_level_category"] = int(current_category_info["id"])
                    
                elif current_category_info["level"] == "second":
                    # temp_property["second_level_category"] = current_category_info["category"]
                    # temp_property["first_level_category"] = self.__category_name_to_category[current_category_info["parent"]]["category"]
                    temp_property["first_level_category"] = int(self.__category_name_to_category[current_category_info["parent"]]["id"])
                    
                
                if current_url not in url_to_embedding_dict:
                    self.__logger.debug(f'current_url {current_url} have no embedding ')
                    continue
                current_embedding_info = url_to_embedding_dict[current_url]
                if metadata is True:
                    summary_temp_property = temp_property.copy()
                    summary_temp_property["subdoc_index"] = -1

                summary_uuid = self.generate_deterministic_id_according_url(f'{current_url}_{-1}')
                url_to_success_info[current_url]["cloud_id"] = int(current_article["cloud_id"])
                url_to_success_info[current_url]["uuids"] = dict()

                try:
                    self.__client.batch.add_data_object(
                        data_object = summary_temp_property,
                        class_name=schema_class,
                        uuid=summary_uuid,
                        vector=current_embedding_info["embeddings"]
                    )                
                    url_to_success_info[current_url]["uuids"]["-1"] = summary_uuid
                except Exception as ex:
                    url_to_success_info[current_url]["success"] = False
                    url_to_success_info[current_url]["fail_reasons"].append(f'summary embedding subdoc_index -1 fail {str(ex)}')
                    self.__logger.debug(f'current_url {str(ex)}')
                
                
                if "subdocembeddings"  in current_embedding_info:
                    for current_sub_embedding_info in current_embedding_info["subdocembeddings"]:
                        sub_temp_property = temp_property.copy()
                        current_subdoc_index = current_sub_embedding_info["subdoc_index"]
                        if metadata is True:
                            sub_temp_property["subdoc_index"] = current_subdoc_index

                        sub_uuid = self.generate_deterministic_id_according_url(f'{current_url}_{current_subdoc_index}')
                        
                        try:
                            self.__client.batch.add_data_object(
                                data_object = sub_temp_property,
                                class_name=schema_class,
                                uuid=sub_uuid,
                                vector=current_sub_embedding_info["embeddings"]
                            )
                            url_to_success_info[current_url]["uuids"][str(current_subdoc_index)] = sub_uuid
                        except Exception as ex:
                            url_to_success_info[current_url]["success"] = False
                            url_to_success_info[current_url]["fail_reasons"].append(f'subdoc embedding {current_subdoc_index} fail {str(ex)}')
                            self.__logger.error(f'current_url {str(ex)}')
                            
        return url_to_success_info
    

    
    def construct_where_filter(self,package_range_list= None,start_time=None,end_time=None,
                               major_language=None,category_list = None,url_list=None,
                               filtered_condition=False,cloud_id_list=None):
        """_summary_
        filter_example where_filter = {
        "operator": "And",
        "operands": [{
                "path": ["wordCount"],
                "operator": "GreaterThan",
                "valueInt": 1000
            }, {
                "path": ["title"],
                "operator": "Like",
                "valueText": "*economy*",
            }]
        }

        Args:
            package_range_list (_type_, optional): _description_. Defaults to None.
            start_time (_type_, optional): _description_. Defaults to None.
            end_time (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        conditions = {
            "operator": "And",
            "operands": []
            
        }
        '''
        if filtered_condition is not None:
            if isinstance(filtered_condition,bool) is False:
                raise ValueError("filtered_condition is not bool")
            filtered_condition = {
                "path":["filtered"],
                "operator": "Equal",
                "valueBoolean": filtered_condition
            }
            conditions["operands"].append(filtered_condition)
        
        if package_range_list is not None:
            if isinstance(package_range_list,list) is False:
                raise ValueError("package_range_list is not list") 
            if len(package_range_list) >= 1:
                for current_package in package_range_list:
                    if isinstance(current_package,str) is False:
                        raise ValueError("current_package is not str")
                package_condion = {
                        "operator": "Or",
                        "operands": []
                }
                for current_package_id in package_range_list:
                    current_package_condition = {
                        "path": ["package_id"],
                        "operator": "Equal",
                        "valueText": current_package_id
                    }
                    package_condion["operands"].append(current_package_condition)
                conditions["operands"].append(package_condion)
        
        '''
        if start_time is not None:
            if isinstance(start_time,datetime) is False:
                raise ValueError("start_time is not datetime")
            int_start_time = int(start_time.timestamp() * 1000)
            current_start_time_condition = {
                        "path": ["published_at"],
                        "operator": "GreaterThanEqual",
                        "valueInt": int_start_time
            }
            conditions["operands"].append(current_start_time_condition)
            
        if end_time is not None:
            if isinstance(end_time,datetime) is False:
                raise ValueError("end_time is not datetime")
            int_end_time = int(end_time.timestamp() * 1000)
            current_end_time_condition = {
                        "path": ["published_at"],
                        "operator": "LessThanEqual",
                        "valueInt": int_end_time
            }
            conditions["operands"].append(current_end_time_condition)
        
        '''
        if major_language is not None:
            if isinstance(major_language,RecommendSupportLanguageEnum) is False:
                raise ValueError("major_language is not RecommendSupportLanguageEnum")
            str_recommend_language = RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT.get_langdetect_language_according_recommend_support_language(major_language)
            current_language_condition = {
                        "path": ["major_language"],
                        "operator": "Equal",
                        "valueText": str_recommend_language
            }
            conditions["operands"].append(current_language_condition)
        '''

        if category_list is not None:
            if isinstance(category_list,list) is False:
                raise ValueError("keyword_list is not list")
            for current_category in category_list:
                if isinstance(current_category,str) is False:
                    raise ValueError("current_keyword is not str")
                if current_category not in self.__category_name_to_category:
                    raise ValueError("category_name is not valid category_name")
                
            if len(category_list)>0:
                category_condition = {
                        "operator": "Or",
                        "operands": []
                }
                for current_category in category_list:
                    current_category_info = self.__category_name_to_category[current_category]
                    category_level = current_category_info["level"]
                    if category_level == "first":
                        category_field_path = "first_level_category"
                    else:
                        continue
                    # elif category_level == "second":
                    #    category_field_path = "second_level_category"
                    
                    current_category_condition = {
                        "path": category_field_path,
                        "operator": "Equal",
                        "valueInt": int(current_category_info["id"])
                    }
                    category_condition["operands"].append(current_category_condition)
                    
                if len(category_condition["operands"]) > 0:
                    conditions["operands"].append(category_condition)
        ''' 
        if url_list != None:
            if isinstance(url_list,list) is False:
                raise ValueError("url_list is not list")
            for current_url in url_list:
                if isinstance(current_url,str) is False:
                    raise ValueError("current_url is not str")
                
            if len(url_list) > 0:
                url_conditions = {
                        "operator": "Or",
                        "operands": []
                }
                for current_url in url_list:
                    current_url_condition = {
                        "path": "url",
                        "operator": "Equal",
                        "valueText": current_url
                    }
                    url_conditions["operands"].append(current_url_condition)
                conditions["operands"].append(url_conditions)
        '''    
        
        
        if cloud_id_list is not  None:
            if isinstance(cloud_id_list,list) is False:
                raise ValueError("cloud_id_list is not list")
            for current_cloud_id in cloud_id_list:
                if isinstance(current_cloud_id,int) is False:
                    raise ValueError("current_cloud_id is not in")
                
            if len(cloud_id_list) > 0:
                cloud_id_conditions = {
                        "operator": "Or",
                        "operands": []
                }
                for current_cloud_id in cloud_id_list:
                    # self.__logger.debug(f'current_cloud_id {current_cloud_id}')
                    current_cloud_id_condition = {
                        "path": "cloud_id",
                        "operator": "Equal",
                        "valueInt": current_cloud_id
                    }
                    cloud_id_conditions["operands"].append(current_cloud_id_condition)
                conditions["operands"].append(cloud_id_conditions) 
        return conditions
        
    
    
        
           
    def search_nearest(self,model_name,model_version,limit,major_language,embedding=None,
                       package_range_list=None,start_time=None,end_time=None,
                       category_list=None,url_list=None,filtered_condition=False,cloud_id_list=None):
        """_summary_
        package_range_list,url_list,filtered_condition not support
        Args:
            model_name (_type_): _description_
            model_version (_type_): _description_
            limit (_type_): _description_
            embedding (_type_, optional): _description_. Defaults to None.
            package_range_list (_type_, optional): _description_. Defaults to None.
            start_time (_type_, optional): _description_. Defaults to None.
            end_time (_type_, optional): _description_. Defaults to None.
            major_language (_type_, optional): _description_. Defaults to None.
            category_list (_type_, optional): _description_. Defaults to None.
            url_list (_type_, optional): _description_. Defaults to None.
            filtered_condition (bool, optional): _description_. Defaults to False.

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
            when embedding is not None, the distance and certainty is not None
            [{'subdoc_index': -1, 'url': 'https://www.stereogum.com/2231005/samantha-urbani-one-day-at-a-time/music/', 'uuid': '938b5940-c5e1-5571-848a-69e2b3b41d32', 'distance': None, 'certainty': None}, 
            {'subdoc_index': -1, 'url': 'https://projectswordtoys.blogspot.com/2023/07/cabinet-meeting.html', 'uuid': '3023bc5a-59c2-5587-9864-e5925b4dba3d', 'distance': None, 'certainty': None}]
        """
        embedding_dim = self.__model_tool.valid_model_name_and_version(model_name,model_version)["embedding_dim"]
        self.__model_tool.valid_model_name_and_version(model_name,model_version)
        if embedding is not None:
            if isinstance(embedding,list) is False:
                raise ValueError("embedding is not list")
            # self.__logger.debug(embedding)
            if len(embedding) != embedding_dim:
                raise ValueError(f"current_embedding's dim {len(embedding)} is not equal model's embedding_dim {embedding_dim}")
            for current_value in embedding:
                if isinstance(current_value,float) is False:
                    raise ValueError("current_value is not float")
        if isinstance(limit,int) is False:
            raise ValueError("limit is not number")

        if isinstance(major_language,RecommendSupportLanguageEnum) is False:
            raise ValueError("major_language is not RecommendSupportLanguageEnum")
        str_recommend_language = RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT.get_langdetect_language_according_recommend_support_language(major_language)
            
        schema_class = f'{model_name}_{model_version}_{str_recommend_language}'
        capital_schema_class = self.make_class_name_valid_name(schema_class)
        where_filter = self.construct_where_filter(package_range_list=package_range_list,start_time=start_time,end_time=end_time,
                                                   major_language=major_language,category_list=category_list,url_list=url_list,
                                                   filtered_condition=filtered_condition,cloud_id_list=cloud_id_list)
        self.__logger.debug(f'capital_schema_class {capital_schema_class} filter {where_filter}')
        # self.__logger.debug(f'embedding {embedding}')
        if embedding is None:
            if len(where_filter['operands']) > 0:
                response = (
                    self.__client.query
                    .get(capital_schema_class, ["cloud_id","subdoc_index"])
                    .with_additional(["id","distance","certainty"]) # https://weaviate.io/developers/weaviate/config-refs/distances metrics
                    .with_where(where_filter)
                    .with_limit(limit)
                    .do()
                )
                self.__logger.debug(f'filtered condtions exist,embedding not exist')
            else:
                response = (
                    self.__client.query
                    .get(capital_schema_class, ["cloud_id","subdoc_index"])
                    .with_additional(["id","distance","certainty"]) # https://weaviate.io/developers/weaviate/config-refs/distances metrics
                    .with_limit(limit)
                    .do()
                )
                self.__logger.debug(f'filtered condtions not exist,embedding not exist')
        else:
            if len(where_filter['operands']) > 0:
                response = (
                    self.__client.query
                    .get(capital_schema_class, ["cloud_id","subdoc_index"])
                    .with_near_vector({"vector":embedding})
                    .with_additional(["id","distance","certainty"]) # https://weaviate.io/developers/weaviate/config-refs/distances metrics
                    .with_where(where_filter)
                    .with_limit(limit)
                    .do()
                )
                self.__logger.debug(f'filtered condtions  exist,embedding  exist')
            else:
                response = (
                    self.__client.query
                    .get(capital_schema_class, ["cloud_id","subdoc_index"])
                    .with_near_vector({"vector":embedding})
                    .with_additional(["id","distance","certainty"]) # https://weaviate.io/developers/weaviate/config-refs/distances metrics
                    .with_limit(limit)
                    .do()
                )
                self.__logger.debug(f'filtered condtions not  exist,  embedding exist')
                
        # self.__logger.debug(f'response {response}')
        
        if "errors" in response:
            self.__logger.error(f'response {response}')
            return []
        # capital_schema_class = self.make_class_name_valid_name(schema_class)
        article_list = response["data"]["Get"][capital_schema_class]
        if article_list is None:
            self.__logger.error(f'there is no valid item for filter {where_filter}')
            return []
        for current_article in article_list:
            # self.__logger.debug(current_article)
            # self.__logger.debug('111111111111111111111111')
            current_article['uuid'] = current_article["_additional"]["id"]
            current_article['distance'] = current_article["_additional"]["distance"]
            current_article['certainty'] = current_article["_additional"]["certainty"]
            del current_article["_additional"]
            # self.__logger.debug(current_article)
        return article_list
    
    def make_class_name_valid_name(self,name):
        if isinstance(name,str) is False:
            raise ValueError("name is not str")
        name = name[0].upper() + name[1:]
        name = name.replace('-','_')
        return name
        

        
        
    '''
    def select_same_package_id(self,model_name,model_version,package_id):
        self.__model_tool.valid_model_name_and_version(model_name,model_version)
        if isinstance(package_id,str) is False:
            raise ValueError("package_id is not str")
        schema_class = f'{model_name}_{model_version}'
        where_filter = {
        "path": ["package_id"],
        "operator": "Equal",
        "valueText": package_id
        }
        response = (
            self.__client.query
            .get(schema_class, ["url","subdoc_index"])
            .with_additional(["id","distance"])
            .with_where(where_filter)
            .with_limit(1000)
            .do()
        )
        capital_schema_class = schema_class[0].upper()+schema_class[1:]
        article_list = response["data"]["Get"][capital_schema_class]
        for current_article in article_list:
            current_article['uuid'] = current_article["_additional"]["id"]
            del current_article["_additional"]
        return response["data"]["Get"][capital_schema_class]
    '''
    
    def generate_deterministic_id_according_url(self,url):
        if isinstance(url,str) is False:
            raise ValueError("url is not str")
        str_uuid = generate_uuid5(url)
        return str_uuid
    
    
    def delete_batch_data(self,model_name,model_version,major_language,package_range_list=None,
                          start_time=None,end_time=None,category_list=None,
                          url_list=None,filtered_condition=False,cloud_id_list=None):
        """_summary_
        package_range_list,url_list,filtered_condition not support
        '''
            {
                "dryRun": false,
                "match": {
                    "class": "Dataset",
                    "where": {
                        "operands": null,
                        "operator": "Equal",
                        "path": [
                            "description"
                        ],
                        "valueText": "weather"
                    }
                },
                "output": "verbose",
                "results": {
                    "failed": 0,
                    "limit": 10000,
                    "matches": 2,
                    "objects": [
                        {
                            "id": "1eb28f69-c66e-5411-bad4-4e14412b65cd",
                            "status": "SUCCESS"
                        },
                        {
                            "id": "da217bdd-4c7c-5568-9576-ebefe17688ba",
                            "status": "SUCCESS"
                        }
                    ],
                    "successful": 2
                }
            }
        '''
 

        Args:
            model_name (_type_): _description_
            model_version (_type_): _description_
            dry_run (bool, optional): _description_. Defaults to False.
            package_range_list (_type_, optional): _description_. Defaults to None.
            start_time (_type_, optional): _description_. Defaults to None.
            end_time (_type_, optional): _description_. Defaults to None.
            major_language (_type_, optional): _description_. Defaults to None.
            category_list (_type_, optional): _description_. Defaults to None.
            url_list (_type_, optional): _description_. Defaults to None.
            filtered_condition (bool, optional): _description_. Defaults to False.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
            {
                "cloud_id":{
                    "success": True,
                    "fail_reason": str
                }
            }
        """
        # if isinstance(dry_run,bool) is False:
        #    raise ValueError("dry_run is not bool")
        if isinstance(major_language,RecommendSupportLanguageEnum) is False:
            raise ValueError("major_language is not RecommendSupportLanguageEnum")
        str_recommend_language = RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT.get_langdetect_language_according_recommend_support_language(major_language)
        self.__client.batch.consistency_level = weaviate.data.replication.ConsistencyLevel.ALL  # default QUORUM
        schema_class = f'{model_name}_{model_version}_{str_recommend_language}'
        capital_schema_class = self.make_class_name_valid_name(schema_class)
        cloud_id_to_success = dict()
        while True:
            item_list = self.search_nearest(model_name,model_version,1000,major_language=RecommendSupportLanguageEnum.ENGLISH,
                                package_range_list=package_range_list,start_time=start_time,end_time=end_time,
                                category_list=category_list,url_list=url_list,filtered_condition=filtered_condition,
                                cloud_id_list=cloud_id_list)
            if len(item_list) < 1:
                break
            for current_item in tqdm(item_list,desc=f"delete current select item {capital_schema_class}"):
                cloud_id_to_success[str(current_item["cloud_id"])] = dict()
                try:
                    delete_response = self.__client.data_object.delete(
                        uuid=current_item['uuid'],
                        class_name=capital_schema_class,  # Class of the object to be deleted
                    )
                    # self.__logger.debug(f'delete response {delete_response}')
                    cloud_id_to_success[str(current_item["cloud_id"])]["success"] = True
                except Exception as ex:
                    self.__logger.error(f'error exception: {str(ex)} ')
                    cloud_id_to_success[str(current_item["cloud_id"])]["success"] = False
                    cloud_id_to_success[str(current_item["cloud_id"])]["fail_reason"] = str(ex)
                    
        return cloud_id_to_success     
        
        '''
        if isinstance(major_language,RecommendSupportLanguageEnum) is False:
            raise ValueError("major_language is not RecommendSupportLanguageEnum")
        str_recommend_language = RECOMMEND_SUPPORT_LANGUAGE_TO_LANGDETECT_LANGUAGE_DICT.get_langdetect_language_according_recommend_support_language(major_language)
        
        self.__client.batch.consistency_level = weaviate.data.replication.ConsistencyLevel.ALL  # default QUORUM
        schema_class = f'{model_name}_{model_version}_{str_recommend_language}'
        capital_schema_class = self.make_class_name_valid_name(schema_class)
        # self.__logger.debug(f'delete batch data in {capital_schema_class} class {cloud_id_list}')
        
        where_filter = self.construct_where_filter(package_range_list=package_range_list,start_time=start_time,end_time=end_time,
                                                   major_language=major_language,category_list=category_list,url_list=url_list,
                                                   filtered_condition=filtered_condition)
        count = 1
        summary_result_url_to_success_info = {
            
        }
        self.__logger.debug(f'delete filter {where_filter}')
        while True:
            self.__logger.debug(f'delete filter {where_filter}')
            dry_run_delete_response = self.__client.batch.delete_objects(
                class_name=capital_schema_class,
                # same where operator as in the GraphQL API
                where=where_filter,
                output="verbose",
                dry_run=True,
            )
            matches = dry_run_delete_response["results"]["matches"]
            if matches == 0:
                break
            self.__logger.debug(f"loop delete count {count}")
            count = count + 1
            uuid_set = set()
            for current_object in dry_run_delete_response["results"]["objects"]:
                uuid_set.add(current_object["id"])
                
            uuid_to_cloud_id_dict = dict()
            self.__logger.debug(f"uuid_set {len(uuid_set)}")
            for current_uuid in tqdm(uuid_set):
                current_data_object = self.__client.data_object.get_by_id(
                    current_uuid,
                    class_name=capital_schema_class,
                )
                
                uuid_to_cloud_id_dict[current_uuid] ={
                    "cloud_id":current_data_object["properties"]["cloud_id"],
                    "subdoc_index":current_data_object["properties"]["subdoc_index"]
                }
                
            real_delete_response = self.__client.batch.delete_objects(
                class_name=capital_schema_class,
                # same where operator as in the GraphQL API
                where=where_filter,
                output="verbose",
                dry_run=False,
            )
            for current_object in real_delete_response["results"]["objects"]:
                current_uuid = current_object["id"]
                # self.__logger.debug(current_object["status"])
                if current_object["status"] == "SUCCESS":
                    summary_result_url_to_success_info[uuid_to_cloud_id_dict[current_uuid]["cloud_id"]] = {
                        "success":True
                    }
                else:
                    summary_result_url_to_success_info[uuid_to_cloud_id_dict[current_uuid]["cloud_id"]] = {
                        "success":False
                    }                 
                    
        return  summary_result_url_to_success_info
        '''
    
    '''
    def mark_data_whether_read_according_url(self,model_name,model_version,url_list,whehter_read=False):
        self.__model_tool.valid_model_name_and_version(model_name,model_version)
        if isinstance(url_list,list) is False:
            raise ValueError("url_list is not list")
        if isinstance(whehter_read,bool) is False:
            raise ValueError("whether_read is not bool")
        current_article_list = self.search_nearest(model_name,model_version,limit=len(url_list),url_list=url_list,filtered_condition=None)
        url_to_mark_success = dict()
        schema_class = f'{model_name}_{model_version}'
        for current_article in current_article_list:
            try:
                self.__client.data_object.update(
                    {"filtered":whehter_read},
                    class_name=schema_class,
                    uuid=current_article["uuid"],
                    consistency_level=weaviate.data.replication.ConsistencyLevel.ALL,  # default QUORUM
                )
                url_to_mark_success[current_article["url"]] = {
                    "success":True
                }
            except Exception as ex:
                self.__logger.debug(str(ex))
                url_to_mark_success[current_article["url"]] = {
                    "success":False,
                    "fail_reason":str(ex)
                }
        
        
        for current_url in url_list:
            if current_url not in url_to_mark_success:
                url_to_mark_success[current_url] = {
                    "success": False,
                    "fail_reason":"not exist weaviate"
                }
        return url_to_mark_success
    '''