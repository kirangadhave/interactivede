import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { INotebookTracker } from '@jupyterlab/notebook';
import { LOG } from '../utils';
import { NBWidgetExtension } from './nbExtension';

/**
 * Plugin initializes here
 */
export const plugin: JupyterFrontEndPlugin<void> = {
  id: 'interactivede:plugin',
  autoStart: true,
  requires: [INotebookTracker],
  activate // This is called to activate the plugin
};

function activate(app: JupyterFrontEnd, nbTracker: INotebookTracker) {
  LOG.log('JupyterLab extension interactivede is activated!');
  console.log('JupyterLab extension interactivede is activated!');

  // Instantiate the widget extension which does the setup
  app.docRegistry.addWidgetExtension(
    'notebook',
    new NBWidgetExtension(nbTracker)
  );
}
