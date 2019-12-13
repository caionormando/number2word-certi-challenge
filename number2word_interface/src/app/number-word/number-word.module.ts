import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { NumberWordComponent } from './number-word.component';




@NgModule({
  declarations: [NumberWordComponent],
  imports: [
    CommonModule,
    FormsModule ],
  exports: [NumberWordComponent]
})
export class NumberWordModule { }
