import { Component } from '@angular/core';
import { CommonModule, JsonPipe } from '@angular/common';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import {GraphModule, NgxGraphModule} from "@swimlane/ngx-graph";
import {element} from "protractor";
import {createDiffieHellman} from "crypto";
import {index} from "d3";
// import { python } from 'pythonia'
// import { ChildProcess } from 'child_process';

declare var require: any

interface  myObject{
  name:String;
  edges:Array<number>
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
  graph: myObject[] | null = null;
  info: string = "Oczekiwanie na plik";
  width: number = 1;
  height : number = 1;
  nodes: Array<any>=
    [

  //  {
  //   id: '2',
  //   label: 'B'
  // }, {
  //   id: '3',
  //   label: 'C'
  // }
    ]
   links: Array<any>=[
  //   {
  //   id: 'a',
  //   source: '1',
  //   target: '2',
  //   label: 'is parent of'
  // }, {
  //   id: 'b',
  //   source: '1',
  //   target: '3',
  //   label: 'custom label'
  // }
  ]
  method = "../../methods/resolution_graph.py"

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

  async generateWeightedResolutionGraph() {
    this.width=2000;
    this.height=1000;

    let formText: any = ""

    try {
      formText = await this.getFormText()
    } catch(e) {
      console.error(e)
    }
    // SEND TEXT TO SERVER
    // console.log("TEXT" + formText)
    this.parseGraphJson(formText);
    this.visualizeGraph(this.graph)

  }



  visualizeGraph(graph: myObject[] | null) {
    if (graph == null) return;

    this.info = "JES GRAPH";
    this.nodes = [];
    this.links = [];
    let links_:Array<any>=[];


    graph.forEach((element, index) => {
      let o = {
        id: (index+1),
        label: element.name
      };
      console.log("Element at index", index, ":", element);
      this.nodes.push(o);
    });


    graph.forEach((element, outindex) => {

        element.edges.forEach((element, index) => {
          let l = {
            id: parseInt((outindex+1).toString() + (index+1).toString()),
            source: (outindex + 1).toString(),
            target: element + 1,
            label: outindex.toString() + index.toString()
          }
          links_.push(l)
        })

    });


    console.log(links_)

    links_= links_.filter(
      (value, index, self)=>
        self.findIndex(
          (item) =>
            (item.target === value.target && item.source === value.source) ||
            (item.target === value.source && item.source === value.target)
        ) === index
    )

    this.links=links_;


    console.log("number of connections:",this.links.length)

    console.log("finally", this.nodes);
  }




}
