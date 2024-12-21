import instaloader as il
from instaloader import Post

profile = il.Profile.from_username(il.Instaloader().context, 'maia.sandu')
posts = profile.get_posts()

for post in posts:
    print(post.mediaid, end="\n\n")
    print(post.url, end="\n\n")
    print(post.mediaid_to_shortcode(post.mediaid), end="\n\n")
    nodes = post.get_sidecar_nodes()
    for node in nodes:
        print(node.display_url, end="")