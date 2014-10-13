var labelType, useGradients, nativeTextSupport, animate;

(function() {
  var ua = navigator.userAgent,
      iStuff = ua.match(/iPhone/i) || ua.match(/iPad/i),
      typeOfCanvas = typeof HTMLCanvasElement,
      nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'),
      textSupport = nativeCanvasSupport 
        && (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
  //I'm setting this based on the fact that ExCanvas provides text support for IE
  //and that as of today iPhone/iPad current text support is lame
  labelType = (!nativeCanvasSupport || (textSupport && !iStuff))? 'Native' : 'HTML';
  nativeTextSupport = labelType == 'Native';
  useGradients = nativeCanvasSupport;
  animate = !(iStuff || !nativeCanvasSupport);
})();

var Log = {
  elem: false,
  write: function(text){
    if (!this.elem) 
      this.elem = document.getElementById('log');
    this.elem.innerHTML = text;
    this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
  }
};


function init(){
  // init data
  var json = [
      {
        "adjacencies": [
            "memo_node_21", 
            {
              "nodeTo": "memo_node_1",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_13",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_14",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_15",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_16",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_17",
              "nodeFrom": "memo_node_0",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#83548B",
          "$type": "circle",
          "$dim": 10
        },
        "id": "memo_node_0",
        "name": "memo_node_0"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_2",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_4",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_5",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_6",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_7",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_8",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_10",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_11",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_12",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_13",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_14",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_15",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_16",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_17",
              "nodeFrom": "memo_node_1",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#EBB056",
          "$type": "circle",
          "$dim": 11
        },
        "id": "memo_node_1",
        "name": "memo_node_1"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_5",
              "nodeFrom": "memo_node_2",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_9",
              "nodeFrom": "memo_node_2",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_18",
              "nodeFrom": "memo_node_2",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#416D9C",
          "$type": "circle",
          "$dim": 7
        },
        "id": "memo_node_2",
        "name": "memo_node_2"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_5",
              "nodeFrom": "memo_node_3",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "memo_node_9",
              "nodeFrom": "memo_node_3",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_10",
              "nodeFrom": "memo_node_3",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_12",
              "nodeFrom": "memo_node_3",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#416D9C",
          "$type": "square",
          "$dim": 10
        },
        "id": "memo_node_3",
        "name": "memo_node_3"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "square",
          "$dim": 11
        },
        "id": "memo_node_4",
        "name": "memo_node_4"
      }, {
        "adjacencies": [
          {
            "nodeTo": "memo_node_9",
            "nodeFrom": "memo_node_5",
            "data": {
              "$color": "#909291"
            }
          }
        ],
        "data": {
          "$color": "#C74243",
          "$type": "triangle",
          "$dim": 8
        },
        "id": "memo_node_5",
        "name": "memo_node_5"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_10",
              "nodeFrom": "memo_node_6",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_11",
              "nodeFrom": "memo_node_6",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#83548B",
          "$type": "circle",
          "$dim": 11
        },
        "id": "memo_node_6",
        "name": "memo_node_6"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#EBB056",
          "$type": "triangle",
          "$dim": 12
        },
        "id": "memo_node_7",
        "name": "memo_node_7"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#C74243",
          "$type": "star",
          "$dim": 10
        },
        "id": "memo_node_8",
        "name": "memo_node_8"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "circle",
          "$dim": 12
        },
        "id": "memo_node_9",
        "name": "memo_node_9"
      }, {
        "adjacencies": [
          {
            "nodeTo": "memo_node_11",
            "nodeFrom": "memo_node_10",
            "data": {
              "$color": "#909291"
            }
          }
        ],
        "data": {
          "$color": "#70A35E",
          "$type": "triangle",
          "$dim": 11
        },
        "id": "memo_node_10",
        "name": "memo_node_10"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#70A35E",
          "$type": "circle",
          "$dim": 11
        },
        "id": "memo_node_11",
        "name": "memo_node_11"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "triangle",
          "$dim": 10
        },
        "id": "memo_node_12",
        "name": "memo_node_12"
      }, {
        "adjacencies": [
          {
            "nodeTo": "memo_node_14",
            "nodeFrom": "memo_node_13",
            "data": {
              "$color": "#557EAA"
            }
          }
        ],
        "data": {
          "$color": "#EBB056",
          "$type": "star",
          "$dim": 7
        },
        "id": "memo_node_13",
        "name": "memo_node_13"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#EBB056",
          "$type": "triangle",
          "$dim": 12
        },
        "id": "memo_node_14",
        "name": "memo_node_14"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_16",
              "nodeFrom": "memo_node_15",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_17",
              "nodeFrom": "memo_node_15",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#83548B",
          "$type": "triangle",
          "$dim": 11
        },
        "id": "memo_node_15",
        "name": "memo_node_15"
      }, {
        "adjacencies": [
          {
            "nodeTo": "memo_node_17",
            "nodeFrom": "memo_node_16",
            "data": {
              "$color": "#557EAA"
            }
          }
        ],
        "data": {
          "$color": "#C74243",
          "$type": "star",
          "$dim": 7
        },
        "id": "memo_node_16",
        "name": "memo_node_16"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#416D9C",
          "$type": "circle",
          "$dim": 7
        },
        "id": "memo_node_17",
        "name": "memo_node_17"
      }, {
        "adjacencies": [
            {
              "nodeTo": "memo_node_19",
              "nodeFrom": "memo_node_18",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "memo_node_20",
              "nodeFrom": "memo_node_18",
              "data": {
                "$color": "#557EAA"
              }
            }
        ],
        "data": {
          "$color": "#EBB056",
          "$type": "triangle",
          "$dim": 9
        },
        "id": "memo_node_18",
        "name": "memo_node_18"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#70A35E",
          "$type": "circle",
          "$dim": 8
        },
        "id": "memo_node_19",
        "name": "memo_node_19"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#C74243",
          "$type": "star",
          "$dim": 8
        },
        "id": "memo_node_20",
        "name": "memo_node_20"
      }
  ];
  // end
  // init ForceDirected
  var fd = new $jit.ForceDirected({
    //id of the visualization container
    injectInto: 'infovis',
    //Enable zooming and panning
    //by scrolling and DnD
    Navigation: {
      enable: true,
      //Enable panning events only if we're dragging the empty
      //canvas (and not a node).
      panning: 'avoid nodes',
      zooming: 10 //zoom speed. higher is more sensible
    },
    // Change node and edge styles such as
    // color and width.
    // These properties are also set per node
    // with dollar prefixed data-properties in the
    // JSON structure.
    Node: {
      overridable: true
    },
    Edge: {
      overridable: true,
      color: '#23A4FF',
      lineWidth: 0.4
    },
    //Native canvas text styling
    Label: {
      type: labelType, //Native or HTML
      size: 10,
      style: 'bold'
    },
    //Add Tips
    Tips: {
      enable: true,
      onShow: function(tip, node) {
        //count connections
        var count = 0;
        node.eachAdjacency(function() { count++; });
        //display node info in tooltip
        tip.innerHTML = "<div class=\"tip-title\">" + node.name + "</div>"
          + "<div class=\"tip-text\"><b>connections:</b> " + count + "</div>";
      }
    },
    // Add node events
    Events: {
      enable: true,
      type: 'Native',
      //Change cursor style when hovering a node
      onMouseEnter: function() {
        fd.canvas.getElement().style.cursor = 'move';
      },
      onMouseLeave: function() {
        fd.canvas.getElement().style.cursor = '';
      },
      //Update node positions when dragged
      onDragMove: function(node, eventInfo, e) {
          var pos = eventInfo.getPos();
          node.pos.setc(pos.x, pos.y);
          fd.plot();
      },
      //Implement the same handler for touchscreens
      onTouchMove: function(node, eventInfo, e) {
        $jit.util.event.stop(e); //stop default touchmove event
        this.onDragMove(node, eventInfo, e);
      },
      //Add also a click handler to nodes
      onClick: function(node) {
        if(!node) return;
        // Build the right column relations list.
        // This is done by traversing the clicked node connections.
        var html = "<h4>" + node.name + "</h4><b> connections:</b><ul><li>",
            list = [];
        node.eachAdjacency(function(adj){
          list.push(adj.nodeTo.name);
        });
        //append connections information
        $jit.id('inner-details').innerHTML = html + list.join("</li><li>") + "</li></ul>";
      }
    },
    //Number of iterations for the FD algorithm
    iterations: 200,
    //Edge length
    levelDistance: 130,
    // Add text to the labels. This method is only triggered
    // on label creation and only for DOM labels (not native canvas ones).
    onCreateLabel: function(domElement, node){
      domElement.innerHTML = node.name;
      var style = domElement.style;
      style.fontSize = "0.8em";
      style.color = "#ddd";
    },
    // Change node styles when DOM labels are placed
    // or moved.
    onPlaceLabel: function(domElement, node){
      var style = domElement.style;
      var left = parseInt(style.left);
      var top = parseInt(style.top);
      var w = domElement.offsetWidth;
      style.left = (left - w / 2) + 'px';
      style.top = (top + 10) + 'px';
      style.display = '';
    }
  });
  // load JSON data.
  fd.loadJSON(json);
  // compute positions incrementally and animate.
  fd.computeIncremental({
    iter: 40,
    property: 'end',
    onStep: function(perc){
      Log.write(perc + '% loaded...');
    },
    onComplete: function(){
      Log.write('done');
      fd.animate({
        modes: ['linear'],
        transition: $jit.Trans.Elastic.easeOut,
        duration: 2500
      });
    }
  });
  // end
}
