import { TestBed } from '@angular/core/testing';

import { NumberWordService } from './number-word.service';

describe('NumberWordService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: NumberWordService = TestBed.get(NumberWordService);
    expect(service).toBeTruthy();
  });
});
