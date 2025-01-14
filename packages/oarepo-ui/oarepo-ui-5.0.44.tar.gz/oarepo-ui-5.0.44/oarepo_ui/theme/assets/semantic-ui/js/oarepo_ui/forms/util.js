import { loadComponents } from "@js/invenio_theme/templates";
import _camelCase from "lodash/camelCase";
import React from "react";
import ReactDOM from "react-dom";
import { getInputFromDOM } from "@js/oarepo_ui";
import { FormConfigProvider } from "./contexts";
import { Container } from "semantic-ui-react";
import { BrowserRouter as Router } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import Overridable, {
  OverridableContext,
  overrideStore,
} from "react-overridable";

/**
 * Initialize Formik form application.
 * @function
 * @param {object} defaultComponents - default components to load if no overriden have been registered.
 * @param {boolean} autoInit - if true then the application is getting registered to the DOM.
 * @returns {object} renderable React object
 */

const queryClient = new QueryClient();
export function createFormAppInit(
  defaultComponents,
  autoInit = true,
  ContainerComponent = React.Fragment
) {
  const initFormApp = (rootElement) => {
    const record = getInputFromDOM("record");
    const formConfig = getInputFromDOM("form-config");
    const recordPermissions = getInputFromDOM("record-permissions");
    const links = getInputFromDOM("links")

    console.debug("Initializing Formik form app...");
    console.debug(
      "[record]:",
      record,
      "\n[formConfig]",
      formConfig,
      "\n[recordPermissions]",
      recordPermissions,
      "\n[UI links]",
      links
    );

    loadComponents("", defaultComponents).then((res) => {
      ReactDOM.render(
        <ContainerComponent>
          <QueryClientProvider client={queryClient}>
            <Router>
              <OverridableContext.Provider value={overrideStore.getAll()}>
                <FormConfigProvider
                  value={{ record, formConfig, recordPermissions, links }}
                >
                  <Overridable id="FormApp.layout">
                    <Container fluid>
                      <p>
                        Provide your form components here by overriding
                        component id "FormApp.layout"
                      </p>
                    </Container>
                  </Overridable>
                </FormConfigProvider>
              </OverridableContext.Provider>
            </Router>
          </QueryClientProvider>
        </ContainerComponent>,
        rootElement
      );
    });
  };

  if (autoInit) {
    const appRoot = document.getElementById("form-app");
    initFormApp(appRoot);
  } else {
    return initFormApp;
  }
}

export const invokeCallbacks = (callbacks, ...args) => {
  let result
  if (!Array.isArray(callbacks)) {
    callbacks = [callbacks];
  }
  callbacks.forEach(callback => {
    if (typeof callback === 'function') {
      // TODO: can this be improved?
      result = callback(...args);
    }
  });

  return result
}