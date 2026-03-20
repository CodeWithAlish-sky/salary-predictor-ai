$port = 8080
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()

Write-Host "Server successfully deployed at http://localhost:$port/" -ForegroundColor Green

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        Write-Host "Received request for $($request.RawUrl)"

        if ($request.RawUrl -eq "/" -or $request.RawUrl -match "index\.html") {
            $path = "Deployed_App.html"
            $response.ContentType = "text/html"
            $content = Get-Content -Path $path -Raw
        } else {
            $response.StatusCode = 404
            $content = "Not Found"
        }

        $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
        $response.ContentLength64 = $buffer.Length
        $output = $response.OutputStream
        $output.Write($buffer, 0, $buffer.Length)
        $output.Close()
    }
} finally {
    $listener.Stop()
}
