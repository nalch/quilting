import { inject, LogManager } from 'aurelia-framework';
import { Config } from 'aurelia-api';

const logger = LogManager.getLogger('tutorial');

@inject(Config)
export class Tutorial {
  constructor(config) {
    this.api = config.getEndpoint('api');
  }

  bind() {
    this.api.find('tutorials')
      .then((tutorials) => {
        this.tutorials = tutorials;
        this.tutorial = tutorials[0];
      })
      .catch(logger.error);
  }

}
