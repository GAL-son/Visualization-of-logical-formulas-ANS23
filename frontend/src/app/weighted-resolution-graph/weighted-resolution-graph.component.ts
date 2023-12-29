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
  graph: Object | null = null;
  info: string = "Oczekiwanie na plik";
  method = "../../methods/resolution_graph.py"

  onChange(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      this.file = file;
    }
  }

  async generateWeightedResolutionGraph() {
    const text = ''
    try {
      // Get graph file data
      const text = await this.file?.text();
      this.info = "Dodano";
      console.log(text)      
    } catch (e) {
      console.error(e)
      this.info = "BŁĄD"
      return
    }

    this.runPythonScript("../../pipeline.py", [text])

    return
   
    try {
      console.log(JSON.parse(text));
      this.graph = JSON.parse(text);
    } catch(e) {
      console.error(e)
      this.info = "BŁĄD"
      return
    }
    console.log(this.graph)
    console.info("TUTAJ")
  }

  visualizeGraph(graph: Object) {

  }

  async getPythonGraph(text: string) {
    

  }

  runPythonScript(scriptPath: any, args: Array<any>) {
    const { spawn } = require('child_process');

    // Use child_process.spawn method from 
    // child_process module and assign it to variable
    const pyProg = spawn('python', [scriptPath].concat(args));
  
    // Collect data from script and print to console
    let data = '';
    pyProg.stdout.on('data', (stdout: any) => {
      data += stdout.toString();
    });
  
    // Print errors to console, if any
    pyProg.stderr.on('data', (stderr: any) => {
      console.log(`stderr: ${stderr}`);
    });
  
    // When script is finished, print collected data
    pyProg.on('close', (code: any) => {
      console.log(`child process exited with code ${code}`);
      console.log(data);
    });
  }
  
}
