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
  info: string = "Awaiting file...";
  width: number = 500;
  height : number = 50;
  maxnodeWidth: number = 55;
  minNodeWith: number = 35;
  labels: boolean = false;

  nodeColor = "#ff0000";
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
      this.info = "File added...";
    }
  }

  handleColor(event: any) {
    const newVal = event.target.value;
    this.nodeColor = newVal.toString()
  }

  handleMaxSize(event: any) {
    const newVal = event.target.value;
    console.log(newVal)
    this.maxnodeWidth = parseInt(newVal)
  }

  handleMinSize(event: any) {
    const newVal = event.target.value;
    console.log(newVal)
    this.minNodeWith = parseInt(newVal)
  }

  handleLabels(event: any) {
    const newLab = event.target.checked;
    this.labels = newLab;
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
    this.info="JSON parsetext-lengthd"
    // console.log("graph paarsed\n"+this.graph)
  }

  async generateWeightedResolutionGraph() {
    const labelsSett = this.labels
    this.labels = false;
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
    setTimeout(() => {
      this.labels = labelsSett
    }, 1000)
  }

  visualizeGraph(graph: myGraph | null) {
    // console.log(graph)
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

    console.log(nodeWeights)

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
  }

  normalizeArray(arr: Array<number>, maxVal: number, minVal: number ) {
    console.info(maxVal)
    console.info(minVal)
    let maxArr =  Math.max.apply(null, arr);
    let minArr =  Math.min.apply(null, arr);

    console.info(arr)

    arr.forEach((val, index) => {
      console.log(val)
      val = ((val - minArr) / (maxArr - minArr)) * (maxVal - minVal) + minVal;
      arr[index] = Math.round(val * 100) / 100;
    });

    console.info(arr)

    return arr
  }




}
