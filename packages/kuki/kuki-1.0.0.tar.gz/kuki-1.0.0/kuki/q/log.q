.log.level:`Info;
.log.formatType:`plain;
.log.stdHandle:1;
.log.errHandle:2;
.log.temporalShortcut:`.z.Z;
.log.jsonHeader:()!();

.log.json:{[handle;level;msgs]
  msg:$[0h=type msgs;" " sv .log.toString each msgs;.log.toString msgs];
  (neg handle) .j.j .log.jsonHeader, `level`timestamp`message!(trim(level);value .log.temporalShortcut;msg);
 };

.log.plain:{[handle;level;msgs]
  msg:$[0h=type msgs;" " sv .log.toString each msgs;.log.toString msgs];
  (neg handle) (string value .log.temporalShortcut)," ",level," ",msg;
 };

.log.log:{[level]
  handle:$[level~"ERROR";.log.errHandle;.log.stdHandle];
  :.log[.log.formatType][handle;level];
 };

.log.Debug:{};

.log.Info:.log.log["INFO "];

.log.Warning:.log.log["WARN "];

.log.Error:.log.log["ERROR"];

.log.refreshLogMethod:{
  .log.Debug:.log.log["DEBUG"];
  .log.Info:.log.log["INFO "];
  .log.Warning:.log.log["WARN "];
  .log.Error:.log.log["ERROR"];
  .log.SetLogLevel .log.level;
 };

.log.SetStdLogFile:{[filepath]
  h:hopen hsym filepath;
  .log.stdHandle:h;
  .log.errHandle:h;
  .log.refreshLogMethod[];
 };

.log.SetErrLogFile:{[filepath]
  h:hopen hsym filepath;
  .log.errHandle:h;
  .log.refreshLogMethod[];
 };

.log.SetConsoleSize:{[consoleSize]
  system"c ", " " sv string $[-6 -6h~type each consoleSize;consoleSize;0 0i] | system"c";
 };

.log.SetConsoleSize[25 320i];

.log.SetDatetimeShortcut:{[shortcut]
  shortcuts: `.z.T`.z.t`.z.Z`.z.z`.z.P`.z.p;
  if[not shortcut in shortcuts;'"Only support temporal types: ", -3!shortcuts];
  .log.temporalShortcut:shortcut;
 };

.log.SetLogFormatType:{[formatType]
  formatTypes: `plain`json;
  if[not formatType in formatTypes;'"Only support log format types: ", -3!formatTypes];
  .log.formatType:formatType;
  .log.refreshLogMethod[];
 };

.log.SetJsonHeader:{[header]
  if[not 11h=type key header;'"Only allow symbol as json header key: ", -3!header];
  .log.jsonHeader:header;
 };

.log.SetLogLevel:{[level]
  levels:`Debug`Info`Warning`Error;
  i:levels?level;
  / if log level is invalid, set level to debug
  .log.level:$[i=count levels;`Debug;level];
  @[`.log;levels@til levels? .log.level;:;{}];
 };

.log.toString:{[msg]$[type[msg] in -10 10h;msg;-3!msg]};
