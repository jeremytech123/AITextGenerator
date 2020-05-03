from src.json_generation.data_preprocessing import DataPrepro
from src.json_generation.prepare_data import prepare_data
from src.utils import *

# Populate the cash metadata first - long operations
# cache = get_metadata_cache()
# cache.populate()

# Extract a book (text and metadata) 
create_file = DataPrepro()
create_file.create_json(b_id=788)

# Create genre
create_file.leave_one_genre()
create_file.stats_genre()

# Apply NER and split data into paragraphs
prepare_data(files=['788'], do_ner=True, do_split=True, verbose=1)

# Summarization script. (Integrate colab notebooks and change paths. Otherwise explain how to do)



"""
# Split into paragraphs
paragraph_preprocessing.separate_paragraphs_all_files(overwrite=False)
parser = paragraph_preprocessing.ParagraphParser(min_threshold=20, min_length=600, max_length=900)
paragraph_preprocessing.separate_in_paragraphs(parser, d_id='1342')

# Create ent_sum template
ent_sum_preprocessing.prepare_json_templates(True)

# Perform NER
model = FlexibleBERTNER(BERT_NER_LARGE, batch_size=128, max_length=2000)
ent_sum_preprocessing.perform_ner_on_file(model)
ent_sum_preprocessing.perform_ner_on_file(model, d_id= '1342')

# Summarise
model_sum = FlexibleBERTSum()
ent_sum_preprocessing.add_summaries([model_sum], replace=True, d_id='120')

"""