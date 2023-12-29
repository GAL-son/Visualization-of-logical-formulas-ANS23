import { Component } from '@angular/core';
import { CommonModule, JsonPipe } from '@angular/common';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
// import { python } from 'pythonia'
// import { ChildProcess } from 'child_process';

declare var require: any


@Component({
  selector: 'app-weighted-resolution-graph',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './weighted-resolution-graph.component.html',
  styleUrl: './weighted-resolution-graph.component.css'
})
export class WeightedResolutionGraphComponent {
  file: File | null = null; // Variable to store file 
  graph: Array<Object> | null = null;
  info: string = "Oczekiwanie na plik";
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
      // console.log(text);
      this.graph = JSON.parse(text);
    } catch(e) {
      console.error(e)
      this.info = "JSON ERROR"
    }
    console.log(this.graph)
  }

  async generateWeightedResolutionGraph() {
    
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

  visualizeGraph(graph: Array<Object> | null) {
    if (graph == null) return

    this.info = "JES GEAPH"

    // console.info(graph.toString())
  }
  
}
