from extractor import DataExtractor
from models import RawRecordModel

def run_pipeline():
    print("Starting the pipeline...")

    #1. Initialize the extractor
    extractor = DataExtractor()

    try:
        #2. Fetch the posts
        posts = extractor.fetch_posts() 
        print(f"Fetched {len(posts)} posts")

        #3. Validate and parse the posts
        validated_posts = []

        for post in posts[:5]: # Get the first 5 posts
            raw_record = RawRecordModel(**post)
            validated_posts.append(raw_record)
            print(f"Validated post: {raw_record.model_dump_json()}")

        print("\nValidated posts:")
        return validated_posts

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()


