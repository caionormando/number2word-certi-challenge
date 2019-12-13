import { Component, OnInit, Input } from "@angular/core";
import { NumberWordService } from "./services/number-word.service";
import { NUMBERWORD } from "./number-word.model";

@Component({
  selector: "app-number-word",
  templateUrl: "./number-word.component.html",
  styleUrls: ["./number-word.component.scss"]
})
export class NumberWordComponent implements OnInit {
  @Input() numberReceived: number;
  word: NUMBERWORD;
  numberArray: Array<number> = [];
  wordsArray: Array<NUMBERWORD> = [];
  constructor(private numberWordService: NumberWordService) {}

  ngOnInit() {

    console.log(this.numberReceived);
    this.getNumberWord(this.numberReceived);
  }

  private getNumberWord(wordNumber: number) {
    this.numberWordService
      .getWordForNumber(wordNumber)
      .subscribe((numberWord: any) => {
        this.word.word = numberWord.extenso;
        this.word.timestamp = new Date();
        this.word.wordNumber = this.numberReceived;
      });
  }

  addFieldValue() {
    this.getNumberWord(this.numberReceived);
    console.log(this.word);
    this.wordsArray.push(this.word);

    this.word = {};
  }

}
