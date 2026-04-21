# Script PowerShell per pubblicare articoli sul blog hcaire
# Esegui dal terminale Windows nella cartella del progetto

$ENDPOINT = "https://depict-gravitate-scrimmage.ngrok-free.dev/api/contents/import"
$TOKEN    = "12969c64bd0742fad24913b1e7190255509c4b4dd3de31937fbd4de9563e0a36"

$headers = @{
    "Authorization"              = "Bearer $TOKEN"
    "Content-Type"               = "application/json; charset=utf-8"
    "ngrok-skip-browser-warning" = "true"
}

function Pubblica-Articolo {
    param (
        [string]$PayloadFile,
        [string]$NomeArticolo
    )

    Write-Host "`n>>> Pubblicazione: $NomeArticolo" -ForegroundColor Cyan

    if (-not (Test-Path $PayloadFile)) {
        Write-Host "    SKIP: payload non trovato ($PayloadFile)" -ForegroundColor Yellow
        return
    }

    # Legge il JSON pre-generato da Python (encoding corretto)
    $body = [System.IO.File]::ReadAllText($PayloadFile, [System.Text.Encoding]::UTF8)

    try {
        $response = Invoke-WebRequest -Uri $ENDPOINT -Method POST -Headers $headers `
                    -Body $body -ErrorAction Stop
        Write-Host "    OK: pubblicato con successo ($($response.StatusCode))" -ForegroundColor Green
        Write-Host "    Risposta: $($response.Content)" -ForegroundColor Gray
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.value__
        $errBody    = $_.ErrorDetails.Message
        if ($statusCode -eq 400 -and $errBody -match "slug") {
            Write-Host "    INFO: articolo gia pubblicato (slug esistente)" -ForegroundColor Yellow
        } else {
            Write-Host "    ERRORE $statusCode : $errBody" -ForegroundColor Red
        }
    }
}

# === LISTA ARTICOLI ===
$payloadsDir = "$PSScriptRoot\payloads"

$articoli = @(
    @{ file = "$payloadsDir\claude-code-master-subprojects.json";            nome = "Claude Code e i Portali Complessi" },
    @{ file = "$payloadsDir\epidemia-solitudine-animismo-tecnologico.json";  nome = "Epidemia di Solitudine e Animismo Tecnologico" },
    @{ file = "$payloadsDir\psicosi-ia-eco-chamber.json";                   nome = "Psicosi da IA e la Trappola dell'Eco-Chamber" },
    @{ file = "$payloadsDir\psicoterapeuta-aumentato.json";                  nome = "Lo Psicoterapeuta Aumentato" },
    @{ file = "$payloadsDir\etica-design-big-tech-educazione-digitale.json"; nome = "Etica del Design e Big Tech" },
    @{ file = "$payloadsDir\vergogna-prometeica-quarta-ferita-narcisistica.json"; nome = "La Quarta Ferita Narcisistica" },
    @{ file = "$payloadsDir\neuroplasticita-addestramento-reciproco-ia.json"; nome = "Neuroplasticita e Addestramento Reciproco" }
)

Write-Host "=== PUBBLICAZIONE ARTICOLI HCAIRE BLOG ===" -ForegroundColor White
Write-Host "Endpoint: $ENDPOINT"
Write-Host "Articoli da pubblicare: $($articoli.Count)"

foreach ($a in $articoli) {
    Pubblica-Articolo -PayloadFile $a.file -NomeArticolo $a.nome
}

Write-Host "`n=== COMPLETATO ===" -ForegroundColor White
