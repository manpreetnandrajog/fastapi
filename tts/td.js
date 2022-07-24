
//<script >
//document.getElementById("myForm");
//.submit();
//</script>

//create a close button and append it to each list item
var myNodelist= document.getElementByTagName("LI");
var i;
for( i=0; i < myNodelist. length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("/u00D7");
    span.classname= " close";
    span.appendChild(txt);
 myNodelist[i].appendChild(span);
}
//submit button
getElementById("myForm");
.submit();


//Click on a close button to hide the current list item
var close= document.getElementByClassName("close");
var i;
for (i=0; i<close.lenght; i++)
{
    close[i].onclick= function(){
        var div = this.parentElement;
        div.style.display= "none";
    }
}

//add a checked symbol when clicking on a list item
var list= document.querySelector("ul");
list.addEventListener('click',function(ev) {
    if (ev.target.tagname === 'LI') {
        ev.target.classlist.toggle('checked');
}
}, false);

//create a new list item whwn clicking on the "add" button
function newElement() {
    var li= document.createElement ("li");
    var inputValue= document.getElementById("my input").value;
    var t=  document.createTextNode(inputValue);
    li.appendChild(t);
    if(inputValue== ''){
        alert (" ARE WE REMEMBERING EVERYTHING THOUGH? 🤔");
    } else {
        document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value= " ";

    var span= document.createElement("SPAN");
    VAR txt= document.createTextNode("/u00D7");
    span.className= " close";
    span.appendChild(txt);
    li.appendChild(span);

    for(i=0;i<close.lenght; i++) {
        close[i].onclick= function() {
            var div= this.parentElement;
            div.style.display= "none";
        }
    }
}


window.onload = () => {
    const form1 = document.querySelector("#addForm");
  
    let items = document.getElementById("items");
    let submit = document.getElementById("submit");
  
    let editItem = null;
  
    form1.addEventListener("submit", addItem);
    items.addEventListener("click", removeItem);
};
  
function addItem(e) {
    e.preventDefault();
  
    if (submit.value != "Submit") {
        console.log("Hello");
  
        editItem.target.parentNode.childNodes[0].data
            = document.getElementById("item").value;
  
        submit.value = "Submit";
        document.getElementById("item").value = "";
  
        document.getElementById("lblsuccess").innerHTML
            = "Text edited successfully";
  
        document.getElementById("lblsuccess")
                        .style.display = "block";
  
        setTimeout(function() {
            document.getElementById("lblsuccess")
                            .style.display = "none";
        }, 3000);
  
        return false;
    }
  
    let newItem = document.getElementById("item").value;
    if (newItem.trim() == "" || newItem.trim() == null)
        return false;
    else
        document.getElementById("item").value = "";
  
    let li = document.createElement("li");
    li.className = "list-group-item";
  
    let deleteButton = document.createElement("button");
  
    deleteButton.className = 
        "btn-danger btn btn-sm float-right delete";
  
    deleteButton.appendChild(document.createTextNode("Delete"));
  
    let editButton = document.createElement("button");
  
    editButton.className = 
            "btn-success btn btn-sm float-right edit";
  
    editButton.appendChild(document.createTextNode("Edit"));
  
    li.appendChild(document.createTextNode(newItem));
    li.appendChild(deleteButton);
    li.appendChild(editButton);
  
    items.appendChild(li);
}
  
function removeItem(e) {
    e.preventDefault();
    if (e.target.classList.contains("delete")) {
        if (confirm("Are you Sure?")) {
            let li = e.target.parentNode;
            items.removeChild(li);
            document.getElementById("lblsuccess").innerHTML
                = "Text deleted successfully";
  
            document.getElementById("lblsuccess")
                        .style.display = "block";
  
            setTimeout(function() {
                document.getElementById("lblsuccess")
                        .style.display = "none";
            }, 3000);
        }
    }
    if (e.target.classList.contains("edit")) {
        document.getElementById("item").value =
            e.target.parentNode.childNodes[0].data;
        submit.value = "EDIT";
        editItem = e;
    }
}
  
function toggleButton(ref, btnID) {
    document.getElementById(btnID).disabled = false;
}