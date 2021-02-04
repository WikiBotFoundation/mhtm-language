### COMMANDS ###
 float == else.import
   command.line(import) == (command.line)
   
  float == else.import 
   createFunction(import) == createFunction
   
   float == else.import
    Main(import) == (Main)
         
    float == else.import
    text/java(import) == (text/java)
    
    float == else.import
    importData(import) == (importData)
    
    float == else.import
    GetURLsystem(import) == (GetURLsystem)
         
    float == else.import
    protocolj(import) == (protocolj)
    
    float == else.import
    getAccesKey(import) == (getAccesKey)
    
    float == else.import
    getComputerExe(import) == (getComputerExe)
   
    float == else.import
    deleteAll(import) == (deleteAll)
    
   ### TOKENS ###
   float == if(commandLine.command.entered)
   float == GetCommandSupport.all(startCommands)
   float == if(createFunction.command.entered)
   float == getFunctionCommand.all
   float == if(main.command.entered)
   float == Main.local(function).text/java
   float == if(text/java.command.entered)
   float == getTextJava(import) symbol(=)
   float == enterText(import) if(textEntered)
   float == createText(import).enteredText
   float == if(GetURLsystem.command.entered)
   float == getURL(import) == url.website
   
     ### BLOCKS ###
     float == else.import
     codeFunction.import
          if(createFunction) symbol() == text="text/java"
      float == textFunction.clickedText
      
      float == else.import
        codeFunction.import
       if(createFunction) symbol () == text="importData"
      float == textFunction.importclickedData
      
      float == else.import
       codeFunction.import
        if(createFunction) symbol() == text="GetURLsystem"
        if(createFunction) symbol [.] == text="text/java"
        if(createFunction) symbol () == text="GetURLsystem"
        if(GetURLsystem) symbol () == text="getURLsystem-token.api"
        token.float == getURLsystem.token
        
        float == else.import
         codeFunction.import
            if(createFunction) symbol() == text="protocolj"
        float == protocol.import
          else == nul.protocol(java)
         domain.getIP(protocol)
          createProtocolServer == import(java)
       float == protocol.server
         getKeyID.server
        
        float == else.import
         codeFunction.import
         if(createFunction) symbol() == text="protocolj"
         if(createFunction) symbol[.] == text="getAccesToken" 
         if(createFunction) symbol (=) == EnteredText.java(enterText) == serverProtocolName
        float == server.ip(locals)
       float == accesKey.ip
            createProtocolServer.ip
       float == protocolServer.ip
         domain. == server.import
       float == accesToken.if(ip)
       
        float == else.import
         codeFunction.import
         if(createFunction) symbol() == text="getComputerExe"
      console.program(import)
          filetype(exe).import(exeFile)
        filetype.console(import.accesToken)
           Computer.exe(console).hector
       
        float == else.import
         codeFunction.import
         if(createFunction) symbol() == text="getComputerExe"
         if(createFunction) symbol [.] == text="deleteAll" 
        console.program(import)
          filetype(exe).import(exeFile)
        filetype.console(import.accesToken)
           Computer.exe(console).hector
       Computer.exe(files).exe
           exe.import(files).hector
         deleteAllFile(.exe)
                Computer.exe(deleteFiles.exe)
              exe.ClearAllData.file(script)
          
