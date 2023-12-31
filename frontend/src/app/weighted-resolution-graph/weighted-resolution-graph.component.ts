import { Component } from '@angular/core';
import { CommonModule, JsonPipe } from '@angular/common';
import { FormControl, ReactiveFormsModule } from '@angular/forms';

import {GraphModule, NgxGraphModule} from "@swimlane/ngx-graph";
import { Subject } from 'rxjs';

interface Node {
  id: string,
  label: string,
  data: {
    weight: number
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
  selector: 'app-weighted-resolution-graph',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, GraphModule],
  templateUrl: './weighted-resolution-graph.component.html',
  styleUrl: './weighted-resolution-graph.component.css'
})

export class WeightedResolutionGraphComponent {
  file: File | null = null; // Variable to store file
  graph: myGraph | null = null;
  info: string = "Awaiting the file";
  width: number = 500;
  height : number = 50;
  maxnodeWidth: number = 20;
  minNodeWith: number = 5;

  nodeColor = "red";
  nodes: Array<any>=[];
  links: Array<any>=[];
  

  zoomToFit$: Subject<boolean> = new Subject();
  fitGraph() {
    this.zoomToFit$.next(true)
  }

  onChange(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      this.file = file;
      this.info = "Dodano";
    }
  }
  getFormText() {
      // Get graph file data
      return this.file?.text().then(x => {
        this.info="Text Extracted"
        return x;
      }
      ).catch(e => {
        console.error(e)
        return e;
      });
  }

  parseGraphJson(text: string) {
    try {
      // console.log(text);
      this.graph = JSON.parse(text);
    } catch(e) {
      console.error(e)
      this.info = "JSON ERROR"
    }
    this.info="JSON parsed"
    // console.log("graph paarsed\n"+this.graph)
  }

  async generateWeightedResolutionGraph() {
    this.info = "GENERATING..."
    let formText: any = ""

    try {
      formText = await this.getFormText()
    } catch(e) {
      console.error(e)
    }
    // SEND TEXT TO SERVER
    // console.log("TEXT" + formText)
    this.parseGraphJson(formText);
    // console.info(this.graph)
    this.visualizeGraph(this.graph)

  }

  visualizeGraph(graph: myGraph | null) {
    this.info = "Visualization in progress..."
    if (graph == null){
      this.info = "ERROR - NO GRAPH PROVIDED"
      return
    }
    // console.log(graph)
    // console.log(graph.links)


    let nodeWeights = new Array<number>(graph.nodes.length)

    graph["nodes"].forEach((node, index) => {
      nodeWeights[index] = node.data.weight
    });

    nodeWeights = this.normalizeArray(nodeWeights, this.maxnodeWidth, this.minNodeWith)
    

    graph["nodes"].forEach((node, index) => {
      node.data.weight = nodeWeights[index]
    });
    console.log("WEIGHTS RECALCULATED")

    if( this.graph?.nodes !== undefined) {
      this.nodes = this.graph?.nodes;  
    }    
    console.log("Nodes appended")

    if( this.graph?.links !== undefined) {
      this.links = this.graph?.links;  
      // console.log(this.links)
    }
    console.log("Links recalculated")

    this.info = "Awaiting NGX GRAPH"

    // // Generate Nodes
    // graph.forEach((element, index) => {
    //   let o = {
    //     id: (index+1),
    //     label: element.name
    //   };
    //   // console.log("Element at index", index, ":", element);
    //   this.nodes.push(o);
    // });

    // let nodeWeights : Array<number> = new Array<number>(this.nodes.length);

    // // Generate Edges + weights
    // graph.forEach((node, outindex) => {
    //   nodeWeights[outindex] = node.edges.length;
    //     node.edges.forEach((element, index) => {
    //       let l = {
    //         id: parseInt((outindex+1).toString() + (index+1).toString()),
    //         source: (outindex + 1).toString(),
    //         target: (element + 1).toString(),
    //         label: outindex.toString() + index.toString()
    //       }
    //       links_.push(l)
    //     })

    // });
    // // console.log(links_)

    // let nodeSize = this.normalizeArray(nodeWeights, this.maxnodeWidth, this.minNodeWith)

    // for (let i = 0; i < this.nodes.length; i++) {
    //   this.nodes[i].data = {
    //     weight: nodeWeights[i],
    //   };

    //   this.nodes[i].width = nodeSize[i];      
    // }

    // console.log(this.nodes)

    // // Remove duplicate Edges
    // links_= links_.filter(
    //   (value, index, self)=>
    //     self.findIndex(
    //       (item) =>
    //         (item.target === value.target && item.source === value.source) ||
    //         (item.target === value.source && item.source === value.target)
    //     ) === index
    // )
    // this.links=links_;
    
    // console.log(this.links)
    // console.log("number of connections:",this.links.length)

    // console.log("finally", this.nodes);

    // Weight data
  }

  normalizeArray(arr: Array<number>, maxVal: number, minVal:number ) {
    let maxArr =  Math.max.apply(null, arr);
    let minArr =  Math.min.apply(null, arr);

    // console.info(arr)

    arr.forEach((val, index) => {
      val = ((val - minArr) / (maxArr - minArr)) * (maxVal - minVal) + minVal;
      arr[index] = Math.round(val * 100) / 100;
    });

    // console.info(arr)

    return arr
  }




}
