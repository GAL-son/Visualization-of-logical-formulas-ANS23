import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {GraphModule, NgxGraphModule} from "@swimlane/ngx-graph";

interface Node {
  id: string,
  label: string,
  data: {
    type: string
    wid: number
    nodeColor: string
  }
}

interface Link {
  id: string,
  source: string,
  target: string
}

interface  myGraph{
  nodes: Array<Node>,
  links: Array<Link>  
}


@Component({
  selector: 'app-resolution-graph-with-reduction',
  standalone: true,
  imports: [CommonModule, GraphModule],
  templateUrl: './resolution-graph-with-reduction.component.html',
  styleUrl: './resolution-graph-with-reduction.component.css'
})



export class ResolutionGraphWithReductionComponent {
  file: File | null = null; // Variable to store file
  graph: myGraph | null = null;
  info: string = "Oczekiwanie na plik";
  width: number = 1;
  height : number = 1;

  labels: boolean = false;
  nodewidth: number = 35;

  nodeColor = "#ff0000";
  groupColor = "#ff9900"
  nodes: Array<any>= []
  links: Array<any>=[]
  // method = "../../methods/graph_reduction.py"//to change?

  onChange(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      this.file = file;
      this.info = "Dodano";
    }
  }

  handleColor(event: any) {
    const newVal = event.target.value;
    this.nodeColor = newVal.toString()
  }

  handleColorGroup(event: any) {
    const newVal = event.target.value;
    this.groupColor = newVal.toString()
  }

  handleSize(event: any) {
    const newVal = event.target.value;
    console.log(newVal)
    this.nodewidth = parseInt(newVal)
  }

  handleLabels(event: any) {
    const newLab = event.target.checked;
    this.labels = newLab;
  }

  getFormText() {
    // Get graph file data
    return this.file?.text().then(x => {
        return x;
      }
    ).catch(e => {
      console.error(e)
      return e;
    });
  }

  parseGraphJson(text: string) {
    try {
      console.log(text);
      this.graph = JSON.parse(text);
    } catch(e) {
      console.error(e)
      this.info = "JSON ERROR"
    }
    console.log("graph paarsed\n"+this.graph)
  }

  async generateReducedResolutionGraph() {
    const labelsSett = this.labels
    this.labels = false;
    this.width=2000;
    this.height=200;

    let formText: any = ""

    try {
      formText = await this.getFormText()
    } catch(e) {
      console.error(e)
    }
    // SEND TEXT TO SERVER
    console.log("TEXT" + formText)
    this.parseGraphJson(formText);
    this.visualizeGraph(this.graph)
    setTimeout(() => {
      this.file = null;
      this.labels = labelsSett
    }, 1000)
  }

  visualizeGraph(graph: myGraph | null) {
    this.info = "Visualization in progress..."
    if (graph == null){
      this.info = "ERROR - NO GRAPH PROVIDED"
      return
    }
    // console.log(graph)
    // console.log(graph.links)


    // let nodeWeights = new Array<number>(graph.nodes.length)

    // graph["nodes"].forEach((node, index) => {
    //   nodeWeights[index] = node.data.weight
    // });

    // // nodeWeights = this.normalizeArray(nodeWeights, this.maxnodeWidth, this.minNodeWith)
    

    graph["nodes"].forEach((node, index) => {
      let type = node.data.type
      node.data.wid = this.nodewidth

      if( type == 'group') {
        node.data.nodeColor = this.groupColor
      } else {
        node.data.nodeColor = this.nodeColor
      }
    });
    // console.log("WEIGHTS RECALCULATED")

    if( this.graph?.nodes !== undefined) {
      this.nodes = this.graph?.nodes;  
    }    
    console.log("Nodes appended")
    console.log(this.nodes)

    if( this.graph?.links !== undefined) {
      this.links = this.graph?.links;  
      // console.log(this.links)
    }
    console.log("Links recalculated")

    this.info = "Awaiting NGX GRAPH"
  }




}
