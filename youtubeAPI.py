# Youtube API Proyect Functions
# Sebastian Quirarte | sebastianquirajus@gmail.com | in/sebastianquirarte | Last Updated: Nov 29 2023

import pandas as pd
import matplotlib.pyplot as plt

def get_channel_stats(youtube, channel_id):
    
    """
    PARAMETERS
    youtube: build object of Youtube API
    channel_id: channel ID
    ---
    RETURNS
    dataframe with channel stats (channel name, subscribers, views, total videos, and playlist ID)
    
    """
    request = youtube.channels().list(
        part = "snippet,contentDetails,statistics",
        id = channel_id
    )
    response = request.execute()

    for item in response['items']:
        data = [{'Channel_Name': item['snippet']['title'],
                'Total_Subscribers': item['statistics']['subscriberCount'],
                'Total_Views': item['statistics']['viewCount'],
                'Total_Videos': item['statistics']['videoCount'],
                'PlaylistID': item['contentDetails']['relatedPlaylists']['uploads']
        }]
    
    return(pd.DataFrame(data))

def get_video_ids(youtube, playlist_id):
    """
    PARAMETERS
    youtube: build object of Youtube API
    playlist_id: playlist ID 
    ---
    RETURNS
    list with all video's IDs
    
    """
    video_ids = []
    
    request = youtube.playlistItems().list(
        part = "snippet,contentDetails",
        playlistId = playlist_id,
        # YouTube API has a max return of 50 values
        maxResults = 50
    )
    response = request.execute()
    
    # Loops through videos in playlist
    for video in response['items']:
        video_ids.append(video['contentDetails']['videoId'])
    
    # This allows us to get ALL video IDs from the channel and not just 50
    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
                    part = 'contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
        response = request.execute()

        for video in response['items']:
            video_ids.append(video['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        
    return video_ids

def get_video_details(youtube, video_ids):
    """
    PARAMETERS
    youtube: build object of Youtube API
    video_ids: list of all video's IDs 
    ---
    RETURNS
    dataframe with stats of each video
        video_id
        channelTitle
        title
        description
        tags
        publishedAt
        viewCount
        likeCount
        commentCount
        duration
        definition
        caption
    
    """
    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    # This avoids an error if data is not available (e.g. no tags added)
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
    
    return pd.DataFrame(all_video_info)

def plot_cloud(wordcloud):
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud) 
    plt.axis("off");

