import React from "react";
import PropTypes from "prop-types";
import { RelatedSelectFieldInternal } from "./RelatedSelectFieldInternal";
import { i18next } from "@translations/oarepo_ui/i18next";
import _reverse from "lodash/reverse";

const defaultSuggestionsSerializer = (suggestions) =>
  suggestions.map((item) => ({
    text: item.title_l10n,
    value: item.id,
    key: item.id,
  }));

export const RelatedSelectField = ({
  fieldPath,
  suggestionAPIUrl,
  suggestionAPIQueryParams,
  suggestionAPIHeaders,
  serializeSuggestions,
  serializeAddedValue,
  initialSuggestions,
  debounceTime,
  noResultsMessage,
  loadingMessage,
  suggestionsErrorMessage,
  noQueryMessage,
  preSearchChange,
  onValueChange,
  search,
  multiple,
  externalSuggestionApi,
  serializeExternalApiSuggestions,
  externalApiButtonContent,
  externalApiModalTitle,
  ...uiProps
}) => {
  return (
    <RelatedSelectFieldInternal
      fluid
      fieldPath={fieldPath}
      suggestionAPIUrl={suggestionAPIUrl}
      selectOnBlur={false}
      suggestionAPIQueryParams={suggestionAPIQueryParams}
      suggestionAPIHeaders={suggestionAPIHeaders}
      serializeSuggestions={serializeSuggestions}
      serializeAddedValue={serializeAddedValue}
      initialSuggestions={initialSuggestions}
      debounceTime={debounceTime}
      noResultsMessage={noResultsMessage}
      loadingMessage={loadingMessage}
      suggestionsErrorMessage={suggestionsErrorMessage}
      noQueryMessage={noQueryMessage}
      preSearchChange={preSearchChange}
      search={search}
      multiple={multiple}
      externalSuggestionApi={externalSuggestionApi}
      serializeExternalApiSuggestions={serializeExternalApiSuggestions}
      externalApiButtonContent={externalApiButtonContent}
      externalApiModalTitle={externalApiModalTitle}
      {...uiProps}
    />
  );
};

RelatedSelectField.propTypes = {
  // List all the props with their respective PropTypes here
  fieldPath: PropTypes.string.isRequired,
  suggestionAPIUrl: PropTypes.string.isRequired,
  suggestionAPIQueryParams: PropTypes.object,
  suggestionAPIHeaders: PropTypes.object,
  serializeSuggestions: PropTypes.func,
  serializeAddedValue: PropTypes.func,
  initialSuggestions: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.object),
    PropTypes.object,
  ]),
  debounceTime: PropTypes.number,
  noResultsMessage: PropTypes.node,
  loadingMessage: PropTypes.string,
  suggestionsErrorMessage: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.object,
  ]),
  noQueryMessage: PropTypes.string,
  preSearchChange: PropTypes.func,
  onValueChange: PropTypes.func,
  search: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
  multiple: PropTypes.bool,
  externalSuggestionApi: PropTypes.string,
  serializeExternalApiSuggestions: PropTypes.func,
  externalApiButtonContent: PropTypes.string,
  externalApiModalTitle: PropTypes.string,
};

// DefaultProps (Optional)
RelatedSelectField.defaultProps = {
  debounceTime: 500,
  suggestionAPIQueryParams: {},
  serializeSuggestions: defaultSuggestionsSerializer,
  suggestionsErrorMessage: i18next.t("Something went wrong..."),
  noQueryMessage: i18next.t("Search..."),
  noResultsMessage: i18next.t("No results found"),
  loadingMessage: i18next.t("Loading..."),
  preSearchChange: (x) => x,
  // search: true,
  multiple: false,
  search: (options) => options,
  initialSuggestions: [],
  suggestionAPIHeaders: {
    Accept: "application/vnd.inveniordm.v1+json",
  },
  externalApiButtonContent: i18next.t("Search External Database"),
  externalApiModalTitle: i18next.t("Search results from external API"),
  serializeExternalApiSuggestions: undefined
};
