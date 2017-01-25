
// BuildCat and countCat are helper functions
// used by showCat and showCatAll
// buildCatList builds a list of links for use by showCat


// Builds cat HTML tags
function buildCat(catName) {

    $('<p>').attr('id', catName+"Output").appendTo('#cats').html('a');
    $('<img>').attr('src', catName+".jpg").attr('id', catName).appendTo('#cats');

}


// Counter function
function countCat(catName) {

  var $catOutput = $('#'+catName+'Output');
  $catOutput.text(catName);

  var $catName = $(catName);
  var catCounter = 0;

  $('#'+catName).click(function(e) {

    console.log(e)
    console.log(catName, "Clicked")

    // updated counter to reflect new click
    catCounter = catCounter + 1
    console.log(catCounter)

    // output times clicked
    console.log($catOutput)

    $catOutput.text(catName + " " + catCounter);

  });
};



function showCatAll() {
  for (var i = 0; i < cats.length; i++) {
      
      buildCat(cats.slice(i, i+1));
      countCat(cats.slice(i, i+1)); 
      console.log(cats.slice(i, i+1));

    };
}


function showCat() {
  
  // get cat
  cat = window.location.hash

  // remove #. Credit to http://stackoverflow.com/questions/3552944/
  var catIndex = cat.indexOf("#")
  var cat = catIndex != -1 ? cat.substring(catIndex+1) : "";
  console.log(cat)

  buildCat(cat);
  countCat(cat);

}


// Builds cat list
function buildCatList() {

    // run through list of cats
    for (var i = 0; i < cats.length; i++) {
      
      // get cat name from list
      catName = cats.slice(i, i+1)
      // create list tag
      var li = $('<li>')
      // create link
      var node =  $('<a>').attr('href', "#"+catName).attr('onClick', "window.location.reload();").html(catName);
      // put link inside list and append to cat list div
      li.append(node).appendTo('#cat-list');

    };
}


var cats = ['Whiskers', 'Symba', 'Kitty'];

// runCatsAll()
buildCatList()
showCat()