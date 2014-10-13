/* ========================================================
 * bootstrap-tabs.js v1.3.0
 * http://twitter.github.com/bootstrap/javascript.html#tabs
 * ========================================================
 * Copyright 2011 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ======================================================== */


(function( $ ){

    function activate ( element, container ) {

        container.find('.active').removeClass('active');
        element.addClass('active');
    }

    function tab( e ) {

        $('#multiImgSwitch').toggleClass('hidden');
        $('#singleImgSwitch').toggleClass('hidden');

        if(e.target.id==="multiImgSwitch") {
            //switch from single to multi-img view
			console.log(slider_event_timeline);
            console.log("from single -> multi");
			//make the single image controls visible
			imageButtons.removeClass("visible");
			imageButtons.addClass("hidden");
			//$('#slider_play').removeclass('visible');
			//$('#slider_play').addclass('hidden');

			//------- Grant can change here start-------
			// Slider or any other feasible components for showing start points of multiple evetns, currently Marissa just created a slider, but it is changable if there are any other feasible components
			slider_event_timeline.removeClass("hidden");
			slider_event_timeline.addClass("visible");
			slide = slider_event_timeline.slider({value:0, min: 0, max: 0, step: 1});
			slide = slider_event_timeline.slider({value:10, min: 0, max: 0, step: 1});
			//------- Grant can change here end-------

            createImageThumbs ();

        } else {
            //switch from multi to single-img view

            //ensure the selected imgs list is empty
            selectedImgs = [];
			imageButtons.removeClass("hidden");
			imageButtons.addClass("visible");
			//$('#slider_play').removeclass('hidden');
			//$('#slider_play').addclass('visible');
			slider_event_timeline.removeClass('visible');
			slider_event_timeline.addClass('hidden');

            console.log("from multi -> single");
        }

        var $this = $(this)
            , href = $this.attr('href')
            , $ul = $(e.liveFired)
            , $controlled

        if (/^#\w+/.test(href)) {
            e.preventDefault()

            if ($this.hasClass('active')) {
                return
            }

            $href = $(href)

            activate($this.parent('div'), $ul)
            activate($href, $href.parent())
        }
    }


    /* TABS/PILLS PLUGIN DEFINITION
     * ============================ */

    $.fn.tabs = $.fn.pills = function ( selector ) {
        return this.each(function () {
            $(this).delegate(selector || '.tabs div > a, .pills > div > a', 'click', tab)
        })
    }

    $(document).ready(function () {
        $('body').tabs('div[data-tabs] div > a, div[data-pills] > div > a')
    })

})( window.jQuery || window.ender )
