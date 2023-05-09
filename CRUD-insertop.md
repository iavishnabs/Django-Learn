## adding datas into table in database
---
* create a add.html file in templates and add a form
* set form method = 'post' and add input field for each fields in table
* add name attribute in each input fields
### views.py in app folder:
* create add function 
* if request.method = 'POST',
* define variables for getting each name attribute from the input form as:

name = request.POST.get('name_in_inputfield')
.............................................

* create a object and assign the table created in model with all the fields=function variables
like:
ob = studentdata(s_name = name,s_course= course) -- studentdata is a table created in models -- s_name and s_course are the fields of this table.
* then saving the object as: ob.save() then redirect to indexpage(which shows the datas as a table in frontend)

### index.html(fetch table datas into frontend)

* create a table and add each fields by context process (

### views.py index functioon define:
d = {
'objects':studentdatas.objects.all()
}
return render(request,'index.html',d)
)

### index.html
{%  for i in objects %}
{{i.s_name}}
{{i.s_course}}
{% endfor %}
