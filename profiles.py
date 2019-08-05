# Finding a profile
def find_profile(username):
    user_profile = {}
    for profile in profiles:
        if profile['username'] == username:
            user_profile = profile

    return user_profile


# Profile list
profiles = [
  {
    'id': 1,
    'username': 'ken_thompson',
    'first_name': 'Ken',
    'last_name': 'Thompson',
    'picture': "https://www.improgrammer.net/wp-content/uploads/2014/02/Ken-Thompson.jpg",
    'friends': [2, 3, 4],
  },
  {
    'id': 2,
    'username': 'dennis_ritchie',
    'first_name': 'Dennis',
    'last_name': 'Ritchie',
    'picture': 'https://www.neowin.net/images/uploaded/brlloct13.jpg',
    'friends': [1, 3, 4],
  }, 
   {
    'id': 3,
    'username': 'james_arthur_gosling',
    'first_name': 'James',
    'last_name': 'Arthur',
    'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/James_Gosling_2005.jpg/250px-James_Gosling_2005.jpg',
    'friends': [1, 2, 4],
  },
  {
    'id': 4,
    'username': 'linus_torvalds',
    'first_name': 'Linus',
    'last_name': 'Torvalds',
    'picture': 'https://images.idgesg.net/images/article/2017/11/linuxcon_europe_linus_torvalds_05-100742477-large.jpg',
    'friends': [1, 2, 3],
  },

  {
    'id': 5,
    'username': 'steve_wozniak',
    'first_name': 'Steve',
    'last_name': 'Wozniak',
    'picture': 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/03/17/12/woz.jpg?w968h681',
    'friends': [6, 7,8],
  },
  {
    'id': 6,
    'username': 'steve_jobs',
    'first_name': 'Steve',
    'last_name': 'Jobs',
    'picture': 'https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Falastairdryburgh%2Ffiles%2F2016%2F07%2Fsteve-jobs-1200x801.jpg',
    'friends': [5, 7],
  },
  {
    'id': 7,
    'username': 'bill_gates',
    'first_name': 'Bill',
    'last_name': 'Gates',
    'picture': 'https://timedotcom.files.wordpress.com/2017/12/bill-gates-inspiring-stories-twitter.jpg',
    'friends': [6, 14, 15],
  },
  {
    'id': 8,
    'username': 'guido_van_rossum',
    'first_name': 'Guido',
    'last_name': 'Van Rossum',
    'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Guido-portrait-2014-curvves.jpg/290px-Guido-portrait-2014-curvves.jpg',
    'friends': [2, 9, 4],
  },
   {
    'id': 9,
    'username': 'brendan_eich',
    'first_name': 'Brendan',
    'last_name': 'Eich',
    'picture': 'https://www.mooncatchermeme.com/wp-content/uploads/sites/11/2018/04/20120226-brendan-eich-001-e1523881303727-740x492.jpg',
    'friends': [3, 8, 4],
  },
  {
    'id': 10,
    'username': 'tim_berners-lee',
    'first_name': 'Tim',
    'last_name': 'Berners-lee',
    'picture': 'https://i1.wp.com/metro.co.uk/wp-content/uploads/2019/03/berners-lee-4405.jpg?quality=90&strip=all&zoom=1&resize=644%2C428&ssl=1',
    'friends': [2, 5, 9],
  },
  {
    'id': 12,
    'username': 'bjarne_stroustrup',
    'first_name': 'Bjarne',
    'last_name': 'Stroustrup',
    'picture': 'https://live.staticflickr.com/4539/37843283924_deae017239_b.jpg',
    'friends': [1, 5, 9],
  },
  {
    'id': 13,
    'username': 'anders_hejlsberg',
    'first_name': 'Anders',
    'last_name': 'Hejlsberg',
    'picture': 'https://cdn.welcometothejungle.co/uploads/video/image/5583/154987/wttj_video_JP6yMV8.jpg',
    'friends': [1, 2, 9],
  },
  {
    'id': 14,
    'username': 'larry_page',
    'first_name': 'Larry',
    'last_name': 'Page',
    'picture': 'https://cdn.androidheadlines.com/wp-content/uploads/2014/10/larry-page-google.jpg',
    'friends': [15, 7, 8],
  },
   {
    'id': 15,
    'username': 'sergey Brin',
    'first_name': 'Sergey',
    'last_name': 'Brin',
    'picture': 'https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2013/googlecofoun.jpg',
    'friends': [14, 7, 8],
  },
   {
    'id': 16,
    'username': 'richard_stallman',
    'first_name': 'Richard',
    'last_name': 'Stallman',
    'picture': 'https://kwygibo.files.wordpress.com/2016/11/richard-stallman-100586957-primary-idge.jpg?w=700',
    'friends': [1, 2, 4],
  }
]