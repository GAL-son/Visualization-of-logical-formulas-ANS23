import { Component } from '@angular/core';

import { WeightedResolutionGraphComponent } from './weighted-resolution-graph/weighted-resolution-graph.component';
import { ResolutionGraphWithReductionComponent } from './resolution-graph-with-reduction/resolution-graph-with-reduction.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    WeightedResolutionGraphComponent,
    ResolutionGraphWithReductionComponent
  ],
  templateUrl: './app.component.template.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'VoLF';
}
