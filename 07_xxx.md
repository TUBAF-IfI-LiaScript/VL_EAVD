<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP.__eval
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s }}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);

    try {
        var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
        var info = log[1] + " " + log[4];

        if (info.length > 80)
          info = info.substring(0,76) + "..."

        error.add_detail(0, info, "error", log[2]-1, log[3]);
    } catch(e) {}

    throw error;
    }
</script>
@end


@JSCPP.eval: @JSCPP.__eval(@input, )

@JSCPP.eval_input: @JSCPP.__eval(@input,`@input(1)`)

@output: <pre class="lia-code-stdout">@0</pre>


script:   https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js

@Rextester.__eval
<script>
//var result = null;
var error  = false;

console.log = function(e){ send.lia("log", JSON.stringify(e), [], true); };

function grep_error(output) {
  let errors = output.match(/:(\d+):(\d+): error: (.+)/g);

  let i = 0;
  for(i = 0; i < errors.length; i++) {
      let e = errors[i].match(/:(\d+):(\d+): error: (.+)/i);

      errors[i] = { row : e[1]-1, column : e[2], text : e[3], type : "error"};
  }
  return errors;
}

function grep_warning(output) {
  let errors = output.match(/:(\d+):(\d+): warning: (.+)/g);

  let i = 0;
  for(i = 0; i < errors.length; i++) {
      let e = errors[i].match(/:(\d+):(\d+): warning: (.+)/i);

      errors[i] = { row: e[1]-1, column : e[2], text : e[3], type : "warning"};
  }
  return errors;
}


$.ajax ({
    url: "https://rextester.com/rundotnet/api",
    type: "POST",
    timeout: 10000,
    data: { LanguageChoice: @0,
            Program: `@input`,
            Input: `@1`,
            CompilerArgs : @2}
    }).done(function(data) {
        if (data.Errors == null) {

/*
            let warnigs = [];

            if(data.Warnings)
              warnings = [grep_warning(data.Warnings)];

            send.lia("log", data.Result+"\n-------------------\n"+data.Stats.replace(/, /g, "\n"), warnings, true);
            send.lia("eval", "LIA: stop");  
*/
            send.lia("eval", data.Result+"\n-------------------\n"+data.Stats.replace(/, /g, "\n"));
        } else {
            let errors = grep_error(data.Errors);

            send.lia("log",
                     data.Errors+"\n-------------------\n"+data.Stats.replace(/, /g, "\n"),
                     [errors], false);

            send.lia("eval", "LIA: stop");
        }
    }).fail(function(data, err) {
        send.lia("log", err, [], false);
        send.lia("eval", "LIA: stop");
    });

"LIA: wait"
</script>
@end


@Rextester.eval: @Rextester.__eval(6, ,"-Wall -std=gnu99 -O2 -o a.out source_file.c")

@Rextester.eval_input: @Rextester.__eval(6,`@input(1)`,"-Wall -std=gnu99 -O2 -o a.out source_file.c")

-->

# Demo


``` c
#include <stdio.h>
#include <stdlib.h>

int main()
{
        int * ptr;

        ptr = malloc(sizeof * ptr);

        if (!ptr) {
                printf("Speicher kann nicht bereitgestellt werden\n");
        } else {
                printf("Speicher bereitgestellt\n");
                * ptr = 70;
                free(ptr);
        }

        return EXIT_SUCCESS;
}
```
@Rextester.eval



```cpp
#include <stdio.h>

int main(void)
{
  int a,b,c;

  printf("Bitte Länge des Quaders eingeben:\n");
  scanf("%d",&a);
  printf("Bitte Breite des Quaders eingeben:\n");
  scanf("%d",&b);
  printf("Bitte Höhe des Quaders eingeben:\n");
  scanf("%d",&c);
  printf("Quaderoberfläche:\n%d\n", 2 * (a * b + a * c + b * c));
  return 0;
}
```
``` bash stdin
2
3
4
```
@Rextester.eval_input
