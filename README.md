# AgileEngine python code challenge

The application must be invoked as follow:
   python app.py reference_file.html check_file.html tag_id

   reference_file.html : is the file containing the tag_id element

   check_file.html : is the file in which the reference element will be found

   the comparison is made atributte by attribute and the return is that tag that has the more
   matches.

   tag_id : this is the id of the element to find in the reference file.


# First run
# Reference File : samples/sample-origin.html
# Check File : samples/sample-1-evil-gemini.html
# Tag id : make-everything-ok-button
# output :

python.exe app.py .\samples\sample-0-origin.html .\samples\sample-4-the-mash.html make-everything-ok-button
2019-08-19 19:05:06,728 Element found:
2019-08-19 19:05:06,728 --------------
2019-08-19 19:05:06,728 <a class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okFinalize(); return false;">
    Do all GREAT
</a>
2019-08-19 19:05:06,729 Path of found tag inside check file:
2019-08-19 19:05:06,729 ------------------------------------
2019-08-19 19:05:06,730 html > body > div > div > div > div > div > div > a


# Second run
# Reference File : samples/sample-origin.html
# Check File : sample-2-container-and-clone.html
# Tag id : make-everything-ok-button
# output :

python.exe app.py .\samples\sample-0-origin.html .\samples\sample-2-container-and-clone.html  make-everything-ok-button
2019-08-19 19:08:16,073 Element found:
2019-08-19 19:08:16,074 --------------
2019-08-19 19:08:16,075 <a class="btn test-link-ok" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okComplete(); return false;">
    Make everything OK
</a>
2019-08-19 19:08:16,075 Path of found tag inside check file:
2019-08-19 19:08:16,075 ------------------------------------
2019-08-19 19:08:16,075 html > body > div > div > div > div > div > div > div > a

# Third run
# Reference File : samples/sample-origin.html
# Check File : sample-3-the-escape.html
# Tag id : make-everything-ok-button
# output :

python.exe app.py .\samples\sample-0-origin.html .\samples\sample-3-the-escape.html make-everything-ok-button
2019-08-19 19:11:47,117 Element found:
2019-08-19 19:11:47,117 --------------
2019-08-19 19:11:47,117 <a class="btn btn-success" href="#ok" title="Do-Link" rel="next" onclick="javascript:window.okDone(); return false;">
    Do anything perfect
</a>
2019-08-19 19:11:47,117 Path of found tag inside check file:
2019-08-19 19:11:47,117 ------------------------------------
2019-08-19 19:11:47,117 html > body > div > div > div > div > div > div > a

# Fourth run
# Reference File : samples/sample-origin.html
# Check File : sample-4-the-mash.html
# Tag id : make-everything-ok-button
# output :

python.exe app.py .\samples\sample-0-origin.html .\samples\sample-4-the-mash.html make-everything-ok-button
2019-08-19 19:13:52,852 Element found:
2019-08-19 19:13:52,852 --------------
2019-08-19 19:13:52,852 <a class="btn btn-success" href="#ok" title="Make-Button" rel="next" onclick="javascript:window.okFinalize(); return false;">
    Do all GREAT
</a>
2019-08-19 19:13:52,852 Path of found tag inside check file:
2019-08-19 19:13:52,852 ------------------------------------
2019-08-19 19:13:52,852 html > body > div > div > div > div > div > div > a