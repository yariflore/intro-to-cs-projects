window.addEventListener("load", function ()
{
   let counter = 0; 
    // variable, keep track of how any times we wil click buttom, keeps track
  //camelCase
   function buttonClicked () 
  {
    counter++;
    
    let clickedCounterElement = document.getElementById("clickcounter");
  
    // document = whole page itself
    //there are different properties inside a document that you can do. getElementById (whatever value u put inthe parentheses) is gonna go to the html file and try to find where you have id= the value you put in
  
  
  clickedCounterElement.innerHTML = "Clicked" + counter + "times.";
    
    //it will replae the content with whatever you want to put inside
  }
  
  let clickedButtonElement = document.getElementById("clickbutton");
  
  clickedButtonElement.addEventListener("click", buttonClicked) ;
   
});
