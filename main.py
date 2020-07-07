import requests
from json import loads
from bs4 import BeautifulSoup
from typing import List

def publication(account: str) -> List[str]:
	base_url = 'https://www.instagram.com/{}/?__a=1'
	request = requests.get(base_url.format(account))
	data = loads(request.text)['graphql']['user']
	data_posts = data['edge_owner_to_timeline_media']['edges']

	post_info = []

	for index in range(len(data_posts)):
		post = data_posts[index]['node']

		display_url = post['display_url']
		comment_count = post['edge_media_to_comment']['count']
		like_count = post['edge_media_preview_like']['count']
		description = '' if not post['edge_media_to_caption']['edges'] \
			else post['edge_media_to_caption']['edges'][0]['node']['text']
		url = f"https://www.instagram.com/p/{post['shortcode']}"

		post_info.append([
			url,
			display_url, 
			like_count, 
			comment_count,
			description
		])
	return post_info

def profile(account: str) -> List[str]:
	base_url = 'https://www.instagram.com/{}/?__a=1'
	request = requests.get(base_url.format(account))
	data = loads(request.text)['graphql']['user']
	post_info = []
	bio = data['biography']
	folow_by = data['edge_followed_by']['count']
	folow = data['edge_follow']['count']
	full_name = data['full_name']
	pr_pic = data['profile_pic_url']
	post_info.append([
		bio,
		folow_by,
		folow,
		full_name,
		pr_pic
		])
	return post_info


def tv(url: str) -> list:
	data = loads(requests.get(f"{url}?__a=1").text)['graphql']['shortcode_media']
	return data['video_url']

