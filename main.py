import os
import json

GHOST_URL = 'https://www.bramadams.dev'

def fetch_posts(json, html = True, pages = False, published = True, visibility = ['public', 'members'], show_tags = True):
    posts = json['db'][0]['data']['posts']
    filtered_posts = []
    for post in posts:
        if published and post['status'] != 'published':
            continue
        if visibility and post['visibility'] not in visibility:
            continue
        post['url'] = GHOST_URL + "/" + post['slug']
        # replace __GHOST_URL__ with the actual URL in all keys
        for key in post:
            if type(post[key]) == str:
                
                post[key] = post[key].replace('__GHOST_URL__', GHOST_URL)
        # filter out the keys that are not relevant to me
        # relevant keys: id, uuid, title, slug, html, plaintext, feature_image, created_at, updated_at, published_at, custom_excerpt

        del post['mobiledoc']
        del post['codeinjection_head']
        del post['codeinjection_foot']
        del post['custom_template']
        del post['canonical_url']
        del post['newsletter_id']
        del post['show_title_and_feature_image']
        del post['featured']
        del post['comment_id']
        del post['status']
        del post['locale']
        del post['lexical']
        del post['visibility']
        del post['email_recipient_filter']

        if show_tags:
            # tags need to be compiled by getting post['id'] and then searching for it in the tags array from the json['db'][0]['data']['posts_tags']
            tags = []
            for post_tag in json['db'][0]['data']['posts_tags']:
                if post_tag['post_id'] == post['id']:
                    tag_id = post_tag['tag_id']
                    for tag in json['db'][0]['data']['tags']:
                        if tag['id'] == tag_id:
                            tags.append(tag['name'])
            post['post_tags'] = str(tags)

        if post['type'] == 'post':
            del post['type']
            filtered_posts.append(post)
        if pages and post['type'] == 'page':
            del post['type']
            filtered_posts.append(post)
    return filtered_posts

def main():
    # pass in filename as first argument
    filename = os.sys.argv[1]
    assert filename.endswith('.json')

    with open(f'{filename}') as f:
        json_str = f.read()
        json_dict = json.loads(json_str)
        
    result = fetch_posts(json_dict)
    # pretty print to json file
    with open('posts.json', 'w') as f:
        json.dump(result, f, indent=4)
    print('Done fetching posts with posts length:', len(result))

if __name__ == '__main__':
    main()
