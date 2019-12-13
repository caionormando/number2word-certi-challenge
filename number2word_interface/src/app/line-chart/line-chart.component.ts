import { Component, Input } from '@angular/core';
import { NUMBERWORD } from '../number-word/number-word.model';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.scss']
})
export class LineChartComponent {
  chartOptions = {
    responsive: true,
    label: "Número"
  };
  label = "Number";
  @Input() chartData: Array<number>;


  onChartClick(event) {
    console.log(event);
  }
}
