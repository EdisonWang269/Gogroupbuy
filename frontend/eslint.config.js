import pluginVue from "eslint-plugin-vue";
export default [
  ...pluginVue.configs["flat/recommended"],
  {
    rules: {
      "vue/padding-lines-in-component-definition": [
        "error",
        {
          betweenOptions: "always" | "never",

          withinOption:
            {
              props:
                {
                  betweenItems: "always" | "never" | "ignore",
                  withinEach: "always" | "never" | "ignore",
                } |
                "always" |
                "never" |
                "ignore", // shortcut to set both

              data:
                {
                  betweenItems: "always" | "never" | "ignore",
                  withinEach: "always" | "never" | "ignore",
                } |
                "always" |
                "never" |
                "ignore", // shortcut to set both

              // ... all options
            } |
            "always" |
            "never" |
            "ignore",

          groupSingleLineProperties: true | false,
        },
      ],
    },
  },
];
