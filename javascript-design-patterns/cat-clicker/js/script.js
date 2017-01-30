
/* 

  Purpose: Start program and run primary function, showCat
  Input: Model, Octopus, View
  Returns: Website with cat clicker

*/

$(function(){

    var model = {
      
      init: function () {
        currentCat = null,
        cats = [
          {
            Name: 'Whiskers',
            ImageURL: 'Whiskers.jpg',
            Count: 0
          },
          {
            Name: 'Symba',
            ImageURL: 'Symba.jpg',
            Count: 0
          },
          {
            Name: 'Kitty',
            ImageURL: 'Kitty.jpg',
            Count: 0
          }
              ]

        // push local storage if doesn't already exist
      if (!localStorage.cats) {
            localStorage.cats = JSON.stringify(cats);
            localStorage.currentCat = currentCat;
        } 
      },        
      
      /* 

        Purpose: Updates Cats array of objects in local storage
        Input: Cat object with variable updates
        Returns: None.

      */
      updateCat: function(cat) {
        
        // get cats
        var catToBeUpdated = cat
        var Cats = model.getCatAll();
        var originalCat = model.getCat(catToBeUpdated);
        console.log("original cat", originalCat)

        originalCat.Count = Number(catToBeUpdated.Count)
          
        //console.log(catToBeUpdated.Count)
        //console.log(Number(catToBeUpdated.Count))

        // Update cat
        for (key in Cats) {
          if (originalCat.Name == Cats[key].Name) {
              Cats[key] = originalCat
          }
        }

        localStorage.cats = JSON.stringify(Cats);
      },

            /* 

        Purpose: Updates Cats array of objects in local storage
        Input: Cat object with variable updates
        Returns: None.

      */
      updateCatAll: function(cat) {
        
        // get cats
        var catToBeUpdated = cat
        var Cats = model.getCatAll();
        var originalCat = model.getCat(catToBeUpdated);
        console.log("original cat", originalCat)

        catToBeUpdated.Count = Number(catToBeUpdated.Count)

        // Update cat
        for (key in Cats) {
          if (originalCat.Name == Cats[key].Name) {
              Cats[key] = catToBeUpdated
          }
        }

        localStorage.cats = JSON.stringify(Cats);
      },
      
      /* 

        Purpose: Get all cats
        Input: None.
        Returns: Cats, an array of cat objects.

      */
      getCatAll: function() {
        var Cats = JSON.parse(localStorage.cats);
        return Cats;
      },  

      /* 

        Purpose: Get single cat object.
        Input: Name of the cat, as a string. ie "Whiskers"
        Returns: Cat object from local storage.

      */
      getCat: function(catName) {

        var Cats = JSON.parse(localStorage.cats);
        for (aCat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(aCat)) {
            if (catName ==  Cats[aCat].Name) {
              cat = Cats[aCat]
              //console.log(cat)
            }
          };
        }

        localStorage.currentCat = catName;
        console.log('local storage update', localStorage.currentCat)

        return cat;
      },


      getCurrentCat: function() {

        var currentCat = localStorage.currentCat;
        console.log("cat from storage", currentCat)
        return currentCat;

      }
    };
    

    var octopus = {
      
      /* 

        Purpose: Count number of times cat clicked.
        Input: Name of the cat, as a string. ie "Whiskers"
        Returns: None.

      */
      countCat: function(catName) {
        
        var cat = model.getCat(catName);
        console.log(cat.Count)

        var $catOutput = $("#"+catName+"Output");
        $catOutput.text(catName + " " + cat.Count);

        $("#"+catName+"Image").click(function(e) {

          console.log(catName, "Clicked")            
          cat.Count = cat.Count + 1
          $catOutput.text(catName + " " + cat.Count);

          model.updateCat({
                Name: cat.Name,
                Count: cat.Count
            });
        });
      },


      /* 

        Purpose: Save cat
        Input: Form data from Admin
        Returns: Updated cat in local storage

      */

      saveCat: function(catName) {
        
        $('form').bind('submit', function (event) {

          event.preventDefault(); // using this page stop being refreshing

          // credit http://stackoverflow.com/questions/169506/obtain-form-input-fields-using-jquery
          var result = { };
          $.each($('form').serializeArray(), function() {
              result[this.name] = this.value;
          });

          console.log(result);
          
          model.updateCatAll(result);

          console.log("Save Clicked");        

        });
      },

      /* 

        Purpose: Show a cat and count it's clicks
        Input: Starts on click of a cat in cat list
        Returns: Cat and cat counter.

      */

      showCat: function() {
        
        $('#cat-list').click(function(e) {

          parantNodeId = e.target.parentNode.id
          if(parantNodeId == 'cat-list') {
            
            var catName = $(e.target).text();
            var cat = model.getCat(catName);

            view.renderCat(catName);
            octopus.countCat(catName);
            view.renderAdmin(catName);

          };
        });
      },


      init: function() {
        model.init()
        view.init()        
      }
    };



    var view = {
      init: function() {
        view.buildCatList()
      },

      /* 

        Purpose: Render visual of cat
        Input: The cat's name catName
        Returns: Cat in html

      */

      renderCat: function(catName) {
          
        var cat = model.getCat(catName);
        // clear old cat
        // TO DO update logic to be use replaceWith function
        $('#cats').find('p').first().remove();
        $('#cats').find('img').first().remove();
        $('<p>').attr('id', catName+"Output").appendTo('#cats').html('a');
        $('<img>').attr('src', cat.ImageURL).attr('id', catName+"Image").appendTo('#cats');

      },

      /* 

        Purpose: Render Admin form
        Input: 
        Returns: 

      */

      renderAdmin: function(catName) {
        
        var cat = model.getCat(catName); 
        var selectACat = 0;
        var fillForm = [];
        fillForm.push(cat.Name, cat.ImageURL, cat.Count);

        /* 
        Finds AdminForm ID, then for each input field, 
        if the inputType is not a submit type, it iterates over each
        It then replaces the value of the input tag where name is equal to name in loop,
        with the value attribute from the array specified above.
        */

        // credit http://stackoverflow.com/questions/5603117/jquery-create-object-from-form-fields
        $("#AdminForm").find("input, text").each(function() {
          var inputType = this.tagName.toUpperCase() === "INPUT" && this.type.toUpperCase();
          
          if (inputType !== "SUBMIT") {
              
              console.log(this.name)
              $('').replaceWith($("input[name='"+this.name+"']").attr('value', fillForm[selectACat]));
              selectACat++;

          }
        });

        octopus.saveCat(cat.Name);
      },


      /* 

        Purpose: Render visual of cat list.
        Input: Data from model.
        Returns: HTML cat list.

      */

      buildCatList: function() {
        
        $('#cat-list').find('li').remove();

        // run through list of cats
        var Cats = model.getCatAll();

        for (cat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(cat)) {
            cat = Cats[cat]
            var li = $('<li>').attr('id', cat.Name).html(cat.Name)
            li.appendTo('#cat-list');
            
            // $('#cat-list').replaceWith($('<li>').attr('id', cat.Name).html(cat.Name));
          }
        };
      }


    };

    octopus.init();
    octopus.showCat();

    // view.renderCat();
    // octopus.countCat();
    // view.renderAdmin();

});