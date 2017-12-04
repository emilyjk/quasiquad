  function checkForm() {
  
  var fname = document.getElementById('fname');
  var lname = document.getElementById('lname');
  var sname = document.getElementById('sname');
  var dname = document.getElementById('dname');
  var title = document.getElementById('title');
  var sess = document.getElementById('sess');
  var nsess = sess.value.length;
  
if (fname.value == "")
    { document.getElementById('fnerror').style.display =     "initial"
    var fname_valid = 0;}
  else if (fname.value != "")
    { document.getElementById('fnerror').style.display =     "none"
    var fname_valid = 1;}
  
if (lname.value == "")
    { document.getElementById('lnerror').style.display =     "initial"
    var lname_valid = 0;}
  else if (lname.value != "")
    { document.getElementById('lnerror').style.display =     "none"
    var lname_valid = 1;}
  
if (sname.value == "")
    { document.getElementById('snerror').style.display =     "initial"
    var sname_valid = 0;}
  else if (sname.value != "")
    { document.getElementById('snerror').style.display =     "none"
    var sname_valid = 1;}
 
  if (dname.value == "")
    { document.getElementById('dnerror').style.display =     "initial"
    var dname_valid = 0;}
  else if (dname.value != "")
    { document.getElementById('dnerror').style.display =     "none"
    var dname_valid = 1;}
  
  if (title.value == "")
    { document.getElementById('titleerror').style.display =     "initial"
    var title_valid = 0;}
  else if (title.value != "")
    { document.getElementById('titleerror').style.display =     "none"
    var title_valid = 1;}
  
  if (nsess <= 99)
    { document.getElementById('sesherror').style.display =     "initial"
    var sess_valid = 0;}
  else if (nsess >= 100)
    { document.getElementById('sesherror').style.display =     "none"
    var sess_valid = 1;}
  
  var light = document.getElementById('lightning')
  var demo = document.getElementById('demo')
  var panel = document.getElementById('panel')
  var poster = document.getElementById('poster')
  if (light.checked == false && demo.checked == false && panel.checked == false && poster.checked == false)
    { document.getElementById('sesserror').style.display =     "initial"
    var sesss_valid = 0;}
  else 
    { document.getElementById('sesserror').style.display =     "none"
    var sesss_valid = 1;}
  
  var fac = document.getElementById('faculty')
  var stu = document.getElementById('student')
  var sta = document.getElementById('staff')
  
  if (fac.checked == false && stu.checked == false && sta.checked == false)
    { document.getElementById('posierror').style.display =     "initial"
    var posi_valid = 0;}
  else 
    { document.getElementById('posierror').style.display =     "none"
    var posi_valid = 1;}
  
  
  if (fname_valid && lname_valid && sname_valid && dname_valid && title_valid && sess_valid && sesss_valid && posi_valid == 1)
    {
      alert("Submitted")
      return true;
    }
  else
  {
return false;
}
}