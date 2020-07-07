# InstaGraBeer
Python instagram parser


# HOW TO USE

**1** publication:

<code>
  from main import publication
  
  name = 'name of user'
  
  print(publication(name))
</code>


**2** profile info:

<code>
  from main import profile
  
  name = 'name of user'
  
  profile(publication(name))
</code>

**3** igtv:

<code>
  from main import tv
  
  link = 'link to igtv'
  
  tv(publication(link))
</code>
