import 'bootstrap/dist/css/bootstrap.css';
import 'font-awesome/css/font-awesome.css';

import { inject, PLATFORM } from 'aurelia-framework';
import { Config } from 'aurelia-api';

@inject(Config)
export class App {
  constructor(config) {
    this.api = config.getEndpoint('api');
  }

  configureRouter(config, router) {
    config.title = 'Quilting';
    config.map([
      { route: '', moduleId: PLATFORM.moduleName('resources/components/tutorial/tutorial'),   title: 'Overview'}
      // { route: 'contacts/:id',  moduleId: PLATFORM.moduleName('contact-detail'), name:'contacts' }
    ]);

    this.router = router;
  }

  bind() {
    this.api.find('tutorials')
      .then((tutorials) => {
        this.tutorials = tutorials;
      });
  }
}
