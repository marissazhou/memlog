/*
 * Author      : Brian Moynagh
 * Created at  : 19-03-2014 
 * Status      : Editable
*/

	var currentAlbum;
        var currentImgNum = 0;
        var lastSelectedDate;
        var playing = false;
        var imageButtons = $(".controls");
        var currentImgTime;
        var selectedImgs = [];
        var selectedImgsIds = [];
        var slide;
        //console.log("=================marissa=================");
		var username 			= document.getElementById("ipt_username").value;
		var album_dates			= JSON.parse(document.getElementById("ipt_album_dates").value);
		var albums 				= JSON.parse(document.getElementById("ipt_albums").value);
		var deleted_image_ids	= []

    //on document ready
    $(document).ready( function() {


    //================================ lazy image loader ===============================================================//


    //======================== Inline Date Picker ======================================================================//

        //set up the date picker
        var datePicker = $('.datepicker').datepicker({

            keyboardNavigation:false,
            format: 'mm/dd/yyyy',

            //**********************************************************************************************************
            //********************* make server call get Album list from the dataBase **********************************
            //**********************************************************************************************************


            beforeShowDay: function (date){

                var day = date.getDate().toString();
                if(day.length<2) {day = "0" + day};

                var month = (date.getMonth()+1).toString();
                if(month.length<2) {month = "0" + month};

                var year = date.getFullYear();

                var theDay = day + '/' + month + '/' + year;
				//album= JSON.parse(album_dates)

                if($.inArray(theDay, album_dates.s) >=0 ) {
                    //console.log(theDay + "Present in s");

                    return {
                        tooltip: 'Album Submitted',
                        classes: 'submitted'
                    };
                }

                if ($.inArray(theDay, album_dates.u) >=0) {
                    //console.log(theDay + "Present in u");
                    return {
                        tooltip: 'Album Not Submitted',
                        classes: 'not-submitted'
                    };

                }

                return false;

            }

        });

        //called when user selects a date
        datePicker.on('changeDate', function(e){

			// start to change date and view
            lastSelectedDate = e.format('dd/mm/yyyy');

            //**********************************************************************************************************
            //********************* make server call get Album from the dataBase ***************************************
            //**********************************************************************************************************

			console.log("change date")
            //get the current album
            //**********************************************************************************************************
            //********************* get the current Album as list 				 ***************************************
            //**********************************************************************************************************
			for (var i=0;i<albums.length;i++)
			{ 
				str1 = JSON.stringify(albums[i].date)
				str2 = JSON.stringify(lastSelectedDate)
				if (str1 == str2)
				{
					currentAlbum = albums[i]
					break;
				}
				else
				{
				}
			}
            //**********************************************************************************************************
            //********************* get the current Album from dict 			 ***************************************
            //**********************************************************************************************************
			/*
			currentAlbum = albums.lastSelectedDate 
			alert("currentAlbum : "+JSON.stringify(currentAlbum));
			*/
			/*
            switch(e.format('dd/mm/yyyy')) {
                case "19/02/2014":  currentAlbum = userAlbum1902; break;
                case "16/12/2013":  currentAlbum = userAlbum1612; break;
                case "17/12/2013":  currentAlbum = userAlbum1712; break;
                case "18/12/2013":  currentAlbum = userAlbum1812; break;
            }
			*/

            //make the single image controls visible
            imageButtons.removeClass("hidden");
            imageButtons.addClass("visible");
            currentImgTime = currentAlbum.images[0].time;

            //show the first image in the current album
            currentImgNum=0;
            $("#singleImg").attr("src", currentAlbum.images[0].src);
            $("#selectedAlbum").html(lastSelectedDate);
            $("#numImages").html(currentAlbum.images.length);
            $("#selectedAlbumStatus").html(currentAlbum.submitted);
            $("#wearTimeEst").html(currentAlbum.wearTime[0].hours + " hrs " + currentAlbum.wearTime[0].minutes + " mins");
            $("#imgTime").html(currentImgTime);

            //set the slider values for the selected Album
            setSliderValues (slide, currentAlbum.images.length-1, 0, currentAlbum.images[currentImgNum].time);

            //bind keys to main window
            $(document).keyup(function(e){

                //console.log(e.which);

                //show next image on x key
                if (e.which == 88 ) {
                    $("#nextImg").click();
                    //alert( "x pressed" );
                    return false;
                }

                //show previous image on z key
                if (e.which == 90) {
                    $("#prevImg").click();
                    //alert( "z pressed" );
                    return false;
                }

                if (e.which == 67) {
                    clearSelectedThumbs();
                    return false;
                }

            });

        });

    //======================== Prev and Next Image buttons =============================================================//

        //next image button
        $("#nextImg").click(function(){
            //console.log(currentImgNum);
            //console.log("next");
            if($("#singleImgView").hasClass('active')) {

                if(currentImgNum+1 < currentAlbum.images.length) {
                    currentImgNum ++;
                    $("#singleImg").attr("src", currentAlbum.images[currentImgNum].src);
                    $("#imgTime").html(currentAlbum.images[currentImgNum].time);
                    slide.slider('setValue', currentImgNum);
                    $(".tooltip-inner").html(currentAlbum.images[currentImgNum].time);
                }

            }

        });

        //previous image button
        $("#prevImg").click(function(){

            if($("#singleImgView").hasClass('active')) {

                if(currentImgNum-1 >= 0) {
                    currentImgNum --;
                    $("#singleImg").attr("src", currentAlbum.images[currentImgNum].src);
                    $("#imgTime").html(currentAlbum.images[currentImgNum].time);
                    slide.slider('setValue', currentImgNum);
                    $(".tooltip-inner").html(currentAlbum.images[currentImgNum].time);
                };

            }
        });

	
        //play button
        $("#playButton").click(function(){

            if($("#singleImgView").hasClass('active')) {

                playing = true;
		
               	 //run 10 times per  second
                 setInterval(function() {
                    if(playing == true) {

                        if(currentImgNum == currentAlbum.images.length-1) {
                            playing = false;
                        } else {
                            $("#nextImg").click();
                        }

                        //console.log("playing");
                    }

                 }, 200)
            }
        });

        //pause button
        $("#pauseButton").click(function(){
                        
             if($("#singleImgView").hasClass('active')) {
                playing = false;

                 console.log("paused");
             }

         });

     //======================== Slider  ================================================================================//

        //set up the slider
        //slide = $('.slider').slider({value:0, min: 0, max: 0, step: 1});
        slide = $('#slider-image').slider({value:0, min: 0, max: 0, step: 1});

        //function that gets called when slide value changes
        slide.on('slide', function(e) {
            currentImgNum = e.value;
            $("#singleImg").attr("src", currentAlbum.images[currentImgNum].src);
            $("#imgTime").html(currentAlbum.images[currentImgNum].time);
            $(".tooltip-inner").html(currentAlbum.images[currentImgNum].time);
        });

    //======================== Delete single Image  ====================================================================//

        $("#imgDelete").click(function() {

            //**********************************************************************************************************
            //********************* make server call to remove the image from the database *****************************
            //********************* save image ids in an array and delete all from database when change date************
            //**********************************************************************************************************
			//console.log(currentAlbum.images)
			//console.log(currentImgNum)
			image_id = currentAlbum.images[currentImgNum].imgId;
			deleted_image_ids.push(image_id)

            //remove the current image from the array
            currentAlbum.images.splice([currentImgNum],1);

            //if user deletes the last image in the album, currentImgNum will be greater than the album length
            //so it needs to be reduced by one so that it still refers to the last image in the album
            if(currentImgNum===currentAlbum.images.length) {
                currentImgNum=currentImgNum-1;
            }

            //get the time of the current image
            currentImgTime = currentAlbum.images[currentImgNum].time;

            // update the view after the image has been deleted
            $("#singleImg").fadeOut('slow', function() {

                //get the src for the next image
                $('#singleImg').attr("src",currentAlbum.images[currentImgNum].src);

                //fade in the new image
                $('#singleImg').fadeIn(200);

                //update the length of the album
                $("#numImages").html(currentAlbum.images.length);

                //update the time of the currently displayed image
                $("#imgTime").html(currentAlbum.images[currentImgNum].time);

                //update the state of the slider
                setSliderValues(slide, currentAlbum.images.length-1,currentImgNum, currentAlbum.images[currentImgNum].time );
            });

        });
    //============================ Tabs ================================================================================//
        $('#tabs').tabs();
    });

    //function to send a command to delete image from the database
	// not tested and used
    function delete_image_backend(imageId) {
		var url = "http://www.google.com/";
		var method = "POST";
		var postData = imageId;
		var async = true;
		var request = new XMLHttpRequest();

		// Before we send anything, we first have to say what we will do when the
		// server responds. This seems backwards (say how we'll respond before we send
		// the request? huh?), but that's how Javascript works.
		// This function attached to the XMLHttpRequest "onload" property specifies how
		// the HTTP response will be handled. 
		request.onload = function () {
		   // Because of javascript's fabulous closure concept, the XMLHttpRequest "request"
		   // object declared above is available in this function even though this function
		   // executes long after the request is sent and long after this function is
		   // instantiated. This fact is CRUCIAL to the workings of XHR in ordinary
		   // applications.

		   // You can get all kinds of information about the HTTP response.
		   var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
		   var data = request.responseText; // Returned data, e.g., an HTML document.
		}

		request.open(method, url, async);
		request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
		// Or... request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
		// Or... whatever

		// Actually sends the request to the server.
		request.send(postData);
    }

    //============================ multiImgView ========================================================================//

    //function to change slider values
    function setSliderValues (slider, sliderMax, sliderValue, tooltiptext) {
            //reset the max value of the slider
            slider.data('slider').max = sliderMax;
            slider.slider('setValue', sliderValue);
            $(".tooltip-inner").html(tooltiptext);
        }

    //function to create image thumbs
    function createImageThumbs () {

        //empty the multi-image div with thumbs
        $('#multiImgDiv').empty();

        //populate the multi-image div with thumbs
        for(var i=0; i<currentAlbum.images.length; i++) {

            var thumb = "<div id='thumb" + i +  "' class='thumb'> </div>";

            var thumbInnerDiv = "<div id = 'thumbInnerDiv" + i + "' class='thumb-inner-div' ></div>";

            var thumbSrc = currentAlbum.images[i].src;

            //--------------------------- will need to infer location of thumb from location of image ----------------//
			var n = thumbSrc.lastIndexOf("/");
			//var n = 16
			//console.log(n);
			//console.log(thumbSrc);
            thumbSrc = thumbSrc.substring(0,n) + "/thumbs" + thumbSrc.substring(n).replace("4.JPG","2.JPG");
			//console.log(thumbSrc);

            var imgThumb =  "<div id='imgWrap"+ i + "' class='img-wrap'> " +
                                "<span id='thumbDelete"+ i +"' class='close' onclick='deleteThumb(this)' ><i class='fa fa-trash-o'></i></span>" +
                                "<img id='thumbImg" + i + "' src ='"+ thumbSrc + "' onclick='selectImg(event)'  style='width:143px; height:107px' >" +
                            "</div>"

            var imgThumbTime = "<div class='thumb-time-div'>"+ currentAlbum.images[i].time +"</div>"

            $('#multiImgDiv').append(thumb);

            $('#thumb' + i).append(thumbInnerDiv);

           $('#thumbInnerDiv' + i).append(imgThumb);

            $('#thumb' + i).append(imgThumbTime );
        }

        console.log("loop done");
    }

    //function to select and un-select an image thumb
    function selectImg(e){

        //get the id of the thumb that was clicked on (e.g thumb0, thumb1,...etc)
        var selectedThumbId = e.toElement.id;

        //get the number of the thumb that was clicked on from its id (e.g. 0,1,2,...etc)
        var selectedImgNum = (selectedThumbId.substring(8))*1;

        // if shift is pressed when user clicks on thumb:
        // then highlight all images between the last selected image and the image that was clicked on when shift was pressed
        if(e.shiftKey) {

            var start = selectedImgs[selectedImgs.length-1] + 1; // next thumb after last entry in the selected images array
            var end = selectedImgNum;

            //handle case of selecting images in reverse order
            if(end < start) {
                start = end;
                end = selectedImgs[0]-1;
            }


            //loop through the thumbs add them to the array selectedImgs and mark the thumbs as selected
            for (var i=start; i<end+1; i++) {

              if(selectedImgs.indexOf(i)<0) {
                selectedImgs.push(i);
                $('#thumb' + i).addClass('selected');
              }

                selectedImgs.sort(function(a,b){return a-b});

            }

        } else {

            //check if the thumb that was clicked on has already been selected:
            //if the image has not been selected it wont be in the array selectedImgs and index will be -1
            var index = selectedImgs.indexOf(selectedImgNum);

            if(index < 0 ) {
                //image was not already selected
                selectedImgs.push(selectedImgNum); //add the number of the image to the array selectedImgs
                selectedImgs.sort(function(a,b){return a-b});
                $('#thumb' + selectedImgNum).addClass('selected'); //show a border around the thumb
            } else {
                //image was already selected
                selectedImgs.splice(index,1); //remove the number of the image from the array selectedImgs
                $('#thumb' + selectedImgNum).removeClass('selected'); //remove the border around the thumb
            }

        }

    }

    //function called when user clicks delete thumb icon
    function deleteThumb(object) {

        if(selectedImgs.length <2) {
            console.log("single");
            deleteSingleThumb(object);

        } else {
            console.log("multi");
            deleteMultipleThumbs();
        }
    }

    //function to delete a single image thumb
    function deleteSingleThumb(object) {

        //the deletedImgNum corresponds to the arrayIndex of the image in currentAlbum.images
        var deletedImgNum = (object.id.substring(11))*1;

        //user deletes the current image in the single image view from the multi image view
        if(deletedImgNum===currentImgNum) {

            console.log("This is a problem");
        }

        //delete image from the array of images
        currentAlbum.images.splice([deletedImgNum],1);

        //**********************************************************************************************************
        //********************* make server call to remove the image from the database *****************************
        //**********************************************************************************************************

        //remove the thumb from the DOM
        $('#thumb' + deletedImgNum).fadeOut('slow', function(){
            $('#thumb' + deletedImgNum).remove();

            //redraw the thumbs
            createImageThumbs();

            //update the length of the album
            $("#numImages").html(currentAlbum.images.length);

            //set slider values
            setSliderValues(slide, (currentAlbum.images.length-1), currentImgNum, currentAlbum.images[currentImgNum].time);
        });

    }

    //function to delete multiple image thumbs
    function deleteMultipleThumbs() {
        console.log (currentAlbum.images);

        //remove images in reverse order
        //the array selectedImgs is a sorted array (low - > high)
        //removing from currentAlbum array in reverse means elements acn be removed from the current AlbumArray
        //without breaking the relationship between the indices of the the currentAlbum array and the selectedImgs array
        for(var i=selectedImgs.length-1; i>=0; i--) {
            console.log("delete img " + selectedImgs[i]);
            console.log( currentAlbum.images[selectedImgs[i]]);

            //delete image from the array of images
            currentAlbum.images.splice(selectedImgs[i],1);

            //remove the thumb from the DOM
            $('#thumb' + selectedImgs[i]).remove();


        }

        //console.log (currentAlbum.images);

        //have to redraw the image thumbs so that thumb0 corresponds to image zero in the currentAlbum Array
        createImageThumbs();

        //update the length of the album
        $("#numImages").html(currentAlbum.images.length);


        //set slider values
        setSliderValues(slide, (currentAlbum.images.length-1), currentImgNum, currentAlbum.images[currentImgNum].time);

        //**********************************************************************************************************
        //********************* make server call to remove the image from the database *****************************
        //**********************************************************************************************************

        //clear the array of selected thumbs
        selectedImgs=[];

    }

    //function to un-select any highlighted thumbs
    function clearSelectedThumbs() {
        if($("#multiImgView").hasClass('active')) {

            for(var i=0; i<selectedImgs.length; i++) {
                $('#thumb' + selectedImgs[i]).removeClass('selected');
            }

            selectedImgs=[];
        }
    }

    function getSelectedImgsIds() {
        imgIds = [];
        for (var i=0; i<selectedImgs.length; i++) {

            imgIds.push((currentAlbum.images)[selectedImgs[i]].imgId);
        }

        return imgIds;
    }


//================================================
//============== select picker ===================
//================================================
$('.selectpicker').selectpicker({
    style: 'btn-info',
    size: 4
});


/*
	general post to url function does things like:
	1. send post to delete image from the database
*/
function post_to_url(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}


/*
	every three seconds, send a POST to the server to update deleted images.
*/
function send_delete_signal_to_server()
{
	setInterval(function(){
		alert("Hello");
		len_del_img = deleted_image_ids.length 
		if (len_del_img > 0){
			post_to_url('/annotater/delete_image', {image_ids:  deleted_image_ids});
			deleted_image_ids = []
		}
	},3000);
}


/*
	keep conducting this command since the page is loaded
*/
//window.onload = send_delete_signal_to_server;

/*
window.onbeforeunload = function(e) {
	console.log("refresh");
	return 'Dialog text here.';
};

$('body').bind('beforeunload',function(){
   //do something
	console.log("refresh");
});
*/

$(window).bind('beforeunload',function(){

     //save info somewhere
    
    return 'are you sure you want to leave?';

});
