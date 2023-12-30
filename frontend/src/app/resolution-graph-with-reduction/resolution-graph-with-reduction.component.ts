import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {GraphModule, NgxGraphModule} from "@swimlane/ngx-graph";

declare var require: any
interface  myObject{
  name:String;
  edges:Array<number>
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
  graph: myObject[] | null = null;
  info: string = "Oczekiwanie na plik";
  width: number = 1;
  height : number = 1;
  nodes: Array<any>= [
    ]
  links: Array<any>=[
  ]
  method = "../../methods/graph_reduction.py"//to change?

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

  async generateReducedResolutionGraph() {
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
          target: (element + 1).toString(),
          label: outindex.toString() + index.toString()
        }
        links_.push(l)
      })

    });


    console.log("Before filtering:", links_);

    links_ = links_.filter(
      (value, index, self) =>
        self.findIndex(
          (item) =>
            (item.target === value.target && item.source === value.source) ||
            (item.target === value.source && item.source === value.target)
        ) === index
    );



    console.log("After filtering:", links_);

    this.links=links_;


    console.log("number of connections:",this.links.length)

    console.log("finally", this.nodes);
  }




}
