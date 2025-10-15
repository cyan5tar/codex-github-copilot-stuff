def send_tweet_with_image(api, message, image_path):
    """
    Sends a tweet with an image.

    Parameters:
    api: The authenticated Twitter API object.
    message (str): The text content of the tweet.
    image_path (str): The file path to the image to be uploaded.

    Returns:
    None
    """
    try:
        # Upload the image
        media = api.media_upload(image_path)
        
        # Post the tweet with the image
        api.update_status(status=message, media_ids=[media.media_id])
        
        print("Tweet sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")