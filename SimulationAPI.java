package raid.hack.crypto.fantom;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import raid.hack.crypto.fantom.response.ExecutionResponse;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

@RestController
public class SimulationAPI {
  private static final String PLAYGROUND_PATH = "../";

  @PostMapping("/api/simulate")
  public ExecutionResponse simulate(
      @RequestParam("code") String mainCode,
      @RequestParam("test") String testCode
  ) {
    String id = CoderHelper.nextIdentifier();
    File mainFile = writeFile(id, "main.py", mainCode);
    File testFile = writeFile(id, "test.py", testCode);
    return execute(new File(PLAYGROUND_PATH, "runner.py").getAbsolutePath(),
        mainFile.getAbsolutePath(),
        testFile.getAbsolutePath());
  }

  @PostMapping("/api/simulate-demo")
  public ExecutionResponse simulateDemo(@RequestParam("demoid") String demoid) {
    return execute(new File(PLAYGROUND_PATH, String.format("demo%d.py", Integer.parseInt(demoid))).getAbsolutePath());
  }


  private File writeFile(String fileId, String format, String code) {
    File file = new File(PLAYGROUND_PATH, fileId + "." + format);
    try (var writer = new BufferedWriter(new FileWriter(file))) {
      writer.write(code);
    } catch (IOException exc) {
      exc.printStackTrace();
    }
    return file;
  }

  private ExecutionResponse execute(String... params) {
    List<String> cmd = new ArrayList<>();
    cmd.add("python3");
//    List<String> cmd = Arrays.asList("sudo", "-u", "unsafe", "python");
    Collections.addAll(cmd, params);
    try {
      return ExecutionController.runAndJoin(cmd.toArray(new String[0]));
    } catch (InterruptedException exc) {
      return null;
    }
  }
}
