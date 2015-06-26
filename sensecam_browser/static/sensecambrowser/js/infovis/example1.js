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
            "Omni Shopping Center", 
            {
              "nodeTo": "DCU",
              "nodeFrom": "Paper",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "cup",
              "nodeFrom": "Paper",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Mobile Phone",
              "nodeFrom": "Paper",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Standing",
              "nodeFrom": "Paper",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Mum's Home",
              "nodeFrom": "Paper",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "printer",
              "nodeFrom": "Paper",
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
        "id": "Paper",
        "name": "Paper"
      }, {
        "adjacencies": [
            {
              "nodeTo": "work",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Henry Street",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "MacBook",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Salmon",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Car Park",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "security",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Howth Junction",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Spar",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Email",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "cup",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Mobile Phone",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Standing",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Mum's Home",
              "nodeFrom": "DCU",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "printer",
              "nodeFrom": "DCU",
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
        "id": "DCU",
        "name": "DCU"
      }, {
        "adjacencies": [
            {
              "nodeTo": "MacBook",
              "nodeFrom": "work",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Mouse",
              "nodeFrom": "work",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Examination",
              "nodeFrom": "work",
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
        "id": "work",
        "name": "work"
      }, {
        "adjacencies": [
            {
              "nodeTo": "MacBook",
              "nodeFrom": "computer",
              "data": {
                "$color": "#909291"
              }
            }, {
              "nodeTo": "Mouse",
              "nodeFrom": "computer",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Howth Junction",
              "nodeFrom": "computer",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Email",
              "nodeFrom": "computer",
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
        "id": "computer",
        "name": "computer"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "square",
          "$dim": 11
        },
        "id": "Henry Street",
        "name": "Henry Street"
      }, {
        "adjacencies": [
          {
            "nodeTo": "Mouse",
            "nodeFrom": "MacBook",
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
        "id": "MacBook",
        "name": "MacBook"
      }, {
        "adjacencies": [
            {
              "nodeTo": "Howth Junction",
              "nodeFrom": "Salmon",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "Spar",
              "nodeFrom": "Salmon",
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
        "id": "Salmon",
        "name": "Salmon"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#EBB056",
          "$type": "triangle",
          "$dim": 12
        },
        "id": "Car Park",
        "name": "Car Park"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#C74243",
          "$type": "star",
          "$dim": 10
        },
        "id": "security",
        "name": "security"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "circle",
          "$dim": 12
        },
        "id": "Mouse",
        "name": "Mouse"
      }, {
        "adjacencies": [
          {
            "nodeTo": "Spar",
            "nodeFrom": "Howth Junction",
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
        "id": "Howth Junction",
        "name": "Howth Junction"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#70A35E",
          "$type": "circle",
          "$dim": 11
        },
        "id": "Spar",
        "name": "Spar"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#83548B",
          "$type": "triangle",
          "$dim": 10
        },
        "id": "Email",
        "name": "Email"
      }, {
        "adjacencies": [
          {
            "nodeTo": "Mobile Phone",
            "nodeFrom": "cup",
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
        "id": "cup",
        "name": "cup"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#EBB056",
          "$type": "triangle",
          "$dim": 12
        },
        "id": "Mobile Phone",
        "name": "Mobile Phone"
      }, {
        "adjacencies": [
            {
              "nodeTo": "Mum's Home",
              "nodeFrom": "Standing",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "printer",
              "nodeFrom": "Standing",
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
        "id": "Standing",
        "name": "Standing"
      }, {
        "adjacencies": [
          {
            "nodeTo": "printer",
            "nodeFrom": "Mum's Home",
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
        "id": "Mum's Home",
        "name": "Mum's Home"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#416D9C",
          "$type": "circle",
          "$dim": 7
        },
        "id": "printer",
        "name": "printer"
      }, {
        "adjacencies": [
            {
              "nodeTo": "Student",
              "nodeFrom": "Examination",
              "data": {
                "$color": "#557EAA"
              }
            }, {
              "nodeTo": "UCD",
              "nodeFrom": "Examination",
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
        "id": "Examination",
        "name": "Examination"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#70A35E",
          "$type": "circle",
          "$dim": 8
        },
        "id": "Student",
        "name": "Student"
      }, {
        "adjacencies": [],
        "data": {
          "$color": "#C74243",
          "$type": "star",
          "$dim": 8
        },
        "id": "UCD",
        "name": "UCD"
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
